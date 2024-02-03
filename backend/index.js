require("dotenv").config();
const express = require("express");
const app = express();
const bodyParser = require("body-parser");
const cookieParser = require("cookie-parser");
const axios = require("axios");
const db = require("./database/db");
const session = require("express-session");
const SequelizeStore = require("connect-session-sequelize")(session.Store);
const cors = require("cors");
const sessionStore = new SequelizeStore({ db });
const runCassandraDB = require("./database/cassandra_db");

app.use(cookieParser());

app.use(
  cors({
    origin: process.env.FRONTEND_URL || process.env.FRONTEND_URL_LOCAL,
    credentials: true,
    allowedHeaders:
      "Authorization, X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version",
    preflightContinue: true,
  })
);

app.use(
  session({
    secret: process.env.SESSION_SECRET,
    store: sessionStore,
    resave: true,
    saveUninitialized: true,
    cookie: {
      maxAge: 2 * 60 * 60 * 1000,
      secure: false,
      httpOnly: false,
      sameSite: false,
    },
  })
);

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.get("/", async (req, res) => {
  const response = await axios.get("http://localhost:5000");

  res.send(response.data);
});

app.use("/auth", require("./auth"));
// app.use("/api", require("./api"));

const severRun = () => {
  app.listen(process.env.PORT, () => {
    console.log(`Listening to PORT: ${process.env.PORT}`);
  });
};

async function main() {
  console.log("Models in the DB:\n", db.models);
  await db.sync();
  await sessionStore.sync();
  await runCassandraDB();
  await severRun();
}

main();
