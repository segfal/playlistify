const router = require("express").Router();
const queryString = require("querystring");
let stateKey = "spotify_auth_state";
const { User } = require("../database/Models");
const axios = require("axios");
const { json } = require("body-parser");

async function logUser(data, req) {
  const access_token = data.access_token;

  try {
    const response = await axios.get(`${process.env.SPOTIFY_BASE_URL}/me`, {
      headers: {
        Authorization: `Bearer ${access_token}`,
      },
    });

    const { display_name, id, email, followers } = response.data;

    const [user, created] = await User.findOrCreate({
      where: { email: email },
      defaults: {
        display_name,
        user_id: id,
        email,
        access_token,
        follower_count: followers.total,
      },
    });

    await user.update({ access_token: access_token });
    await user.save();

    req.session.user = JSON.stringify(user);
  } catch (error) {
    console.error(error);
  }
}

router.get("/", (req, res) => {
  let code = req.query.code || null;
  let state = req.query.state || null;
  let storedState = req.cookies ? req.cookies[stateKey] : null;

  if (state === null || state !== storedState) {
    res.redirect(
      "/#" +
        queryString.stringify({
          error: "state_mismatch",
        })
    );
  } else {
    res.clearCookie(stateKey);

    const authOptions = {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
        Authorization:
          "Basic " +
          Buffer.from(
            process.env.SPOTIFY_CLIENT_ID + ":" + process.env.SPOTIFY_SECRET
          ).toString("base64"),
      },
      body: `code=${code}&redirect_uri=${process.env.SPOTITY_CALLBACK_URL}&grant_type=authorization_code`,
      json: true,
    };

    fetch("https://accounts.spotify.com/api/token", authOptions)
      .then((response) => {
        if (response.status === 200) {
          response.json().then(async (data) => {
            await logUser(data, req);
            res.send({ data });
          });
        }
      })
      .catch((error) => {
        console.log(error);
      });
  }
});

module.exports = router;
