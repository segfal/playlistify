const router = require("express").Router();
const queryString = require("querystring");
let stateKey = "spotify_auth_state";
const { User } = require("../database/Models");
const axios = require("axios");

async function logUser(data) {
  const access_token = data.access_token;

  try {
    const response = await axios.get("https://api.spotify.com/v1/me", {
      headers: {
        Authorization: `Bearer ${access_token}`,
      },
    });

    console.log(response.data);
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
            await logUser(data);
            console.log(`Data: `, data);
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
