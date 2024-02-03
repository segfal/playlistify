const router = require("express").Router();
const querystring = require("querystring");

const getRandomString = (length) => {
  let text = "";
  const possibles =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcedefghijklmnopqrstuvwxyz1234567890";

  for (let i = 0; i < length; i++) {
    text += possibles.charAt(Math.random() * possibles.length);
  }

  return text;
};

let stateKey = "spotify_auth_state";

router.get("/", (req, res) => {
  const state = getRandomString(16);
  const scope =
    "playlist-read-private playlist-read-collaborative user-library-read user-read-email user-read-private user-read-recently-played user-top-read user-read-playback-state";

  res.cookie(stateKey, state);

  res.redirect(
    "https://accounts.spotify.com/authorize?" +
      querystring.stringify({
        response_type: "code",
        client_id: process.env.SPOTIFY_CLIENT_ID,
        scope: scope,
        redirect_uri: process.env.SPOTITY_CALLBACK_URL,
        state: state,
      })
  );
});

module.exports = router;
