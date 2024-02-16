const router = require("express").Router();
const loadUser = require("../middleware/loadUser");
const axios = require("axios");
const { client } = require("../database/cassandra_db");

async function getSongs(items, req) {
  const songsList = [];

  for (let item of items) {
    const artists = item.track.artists.map((artist) => artist.name).join(" ");
    const genresArray = [];
    for (let artist of item.track.artists) {
      try {
        const response = await axios.get(
          `https://api.spotify.com/v1/artists/${artist.id}`,
          {
            headers: {
              Authorization: `Bearer ${req.user.access_token}`,
            },
          }
        );
        genresArray.push(...response.data.genres);
      } catch (error) {
        console.error("Error fetching genres:", error);
      }
    }

    const genres = genresArray.join(",");

    songsList.push({
      artist: artists,
      song: item.track.name,
      genre: genres,
    });
  }

  return songsList;
}

async function getPlaylistList(playlistList, req, next) {
  const formattedPlaylist = [];
  try {
    for (let playlist of playlistList) {
      console.log(`Playlist ${playlist.name}:`);
      const response = await axios.get(
        `https://api.spotify.com/v1/playlists/${playlist.id}`,
        {
          headers: {
            Authorization: `Bearer ${req.user.access_token}`,
          },
        }
      );

      const songs = await getSongs(response.data.tracks.items, req);

      const playlistData = {
        playlist_id: playlist.id,
        songs: await songs,
      };

      formattedPlaylist.push({
        user_id: req.user.user_id,
        playlist: playlistData,
      });

      // Store the playlist data in Cassandra
      await storeDataInCassandra(req.user.user_id, playlistData, next);
    }
  } catch (error) {
    console.log(error);
    next(error);
  }
  return formattedPlaylist;
}

async function storeDataInCassandra(user_id, playlist, next) {
  await client.connect();

  try {
    const playlistJSON = JSON.stringify(playlist);

    const insertQuery =
      "INSERT INTO playlist.playlist_tb (user_id, playlist) VALUES (?, ?)";
    await client.execute(insertQuery, [user_id, playlistJSON]);
    console.log("Playlist data stored successfully.");
  } catch (error) {
    console.error("Error storing playlist data:", error);
    next(error);
  }

  await client.shutdown();
}

router.get("/", loadUser, async (req, res, next) => {
  try {
    const response = await axios.get(
      `https://api.spotify.com/v1/users/${req.user.user_id}/playlists`,
      {
        headers: {
          Authorization: `Bearer ${req.user.access_token}`,
        },
      }
    );

    await getPlaylistList(response.data.items, req, next);

    res.status(200).send("Data retrival successful");
  } catch (error) {
    console.log(error);
    next(error);
  }
});

module.exports = router;
