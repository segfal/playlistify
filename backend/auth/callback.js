const router = require("express").Router();
const queryString = require("querystring");
let stateKey = "spotify_auth_state";
const { User } = require("../database/Models");

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
  }
});

module.exports = router;
