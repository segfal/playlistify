require("dotenv").config();
const { Sequelize } = require("sequelize");
const pg = require("pg");

const db = new Sequelize(`${process.env.POSTGRES_URL}?sslmode=require`, {
  logging: false,
  dialect: pg,
});

db.authenticate()
  .then(() => {
    console.log("DB connection Works");
  })
  .catch((error) => {
    console.log(`DB connection failed:\n ${error}`);
  });

module.exports = db;
