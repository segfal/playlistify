const { DataTypes } = require("sequelize");
const db = require("../db");

const User = db.define("User", {
  username: {
    type: DataTypes.STRING,
    allowNull: false,
    unique: true,
  },
  first_name: {
    type: DataTypes.STRING,
    allowNull: true,
  },
  last_name: {
    type: DataTypes.STRING,
    allowNull: true,
  },
  password: {
    type: DataTypes.STRING,
    allowNull: true,
  },
  access_token: {
    type: DataTypes.STRING,
    allowNull: true,
  },
});

module.exports = User;
