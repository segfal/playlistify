import asyncio
from cassandra.io.libevreactor import LibevConnection
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import json


async def main():
    cloud_config = {"secure_connect_bundle": "secure-connect-playlist-db.zip"}

    with open("playlist_db-token.json") as f:
        secrets = json.load(f)

    CLIENT_ID = secrets["clientId"]
    CLIENT_SECRET = secrets["secret"]

    auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
    cluster = await Cluster.connect_async(
        cloud=cloud_config, auth_provider=auth_provider
    )
    cluster.connection_class = LibevConnection()
    session = cluster.connect()

    row = await session.execute_async("SELECT * FROM playlist.playlist_tb").one()
    if row:
        print(row[0])
    else:
        print("An error occurred.")
