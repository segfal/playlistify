require("dotenv").config();
const { Client } = require("cassandra-driver");
const path = require("path");

const credentials = {
  clientId: process.env.CASSANDRA_CLIENT_ID,
  secret: process.env.CASSANDRA_SECRET,
  token: process.env.CASSANDRA_TOKEN,
};

async function runCassandraDB() {
  const client = new Client({
    cloud: {
      secureConnectBundle: path.resolve(
        __dirname,
        "secure-connect-playlist-db.zip"
      ),
    },
    credentials: {
      username: credentials.clientId,
      password: credentials.secret,
    },
  });

  await client.connect();

  // Execute a query
  const rs = await client.execute("SELECT * FROM playlist.playlist_tb");
  console.log(`Your cluster returned ${rs.rowLength} row(s)`);
  console.dir(rs);

  let properties = rs.columns.map((element) => element.name);
  let tabularData = rs.rows;
  console.log(tabularData, properties);
  console.table(tabularData);

  await client.shutdown();
}

// Run the async function
module.exports = runCassandraDB;
