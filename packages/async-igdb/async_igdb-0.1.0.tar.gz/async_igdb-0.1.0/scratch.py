import asyncio
import json
from typing import Type, get_type_hints
from dotenv import load_dotenv
import os
from async_igdb import IGDBClient
from async_igdb.util import CharacterSpeciesEnum

load_dotenv()


async def main():
    client_id = os.getenv("IGDB_ID")
    client_secret = os.getenv("IGDB_SECRET")

    async with IGDBClient(client_id, client_secret=client_secret) as client:
        results = await client.games.find(limit=100)
        final = [
            i.model_dump(mode="json", warnings=False)
            for i in await client.resolve_links(results, max_depth=1)
        ]
        with open("test.json", "w") as f:
            json.dump(final, f, indent=4)


asyncio.run(main())
