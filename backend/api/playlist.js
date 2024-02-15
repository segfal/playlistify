const router = require("express").Router();
const loadUser = require("../middleware/loadUser");
const axios = require("axios");

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
    console.log("Response: ", response.data);
    res.send("Working");
  } catch (error) {
    console.log(error);
    next(error);
  }
});

module.exports = router;
