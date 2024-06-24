"""A set of helper methods for populating your database with information when you already have an API to extract from.

Simply update the `add_data` method (and your DB model - replacing `ExampleDB`) and run the script directly.
"""

import requests
import asyncio
import aiohttp

from app.config.settings import settings
from app.models import __beanie_models__
from app.models import ExampleDB

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import HTTPException


async def fetch(session: aiohttp.ClientSession, url: str) -> dict:
    """Fetch a single session item asynchronously."""
    async with session.get(url) as res:
        if res.status != 200:
            res.raise_for_status()

        return await res.json()


async def fetch_all(session, urls: dict[str, str]) -> list[dict]:
    """Create the tasks for multiple session requests."""
    tasks = [asyncio.create_task(fetch(session, url)) for url in urls]
    data = await asyncio.gather(*tasks)
    return data


def fetch_one(url: str) -> dict:
    """Fetch a single set of data from a URL."""
    res = requests.get(url)

    if res.status_code == 200:
        return res.json()

    raise requests.HTTPError(f"Request failed with status code: {res.status_code}.")


async def add_data() -> None:
    """A helper method for extracting information from an API and storing them in the database."""
    API_URL = ""  # Must be updated

    client = AsyncIOMotorClient(settings.DB_URL)
    await init_beanie(
        database=client[settings.DB_NAME], document_models=__beanie_models__
    )

    print("Retrieving spells...", end="")
    res = fetch_one(API_URL)
    urls = [
        f"{API_URL}/{item["index"]}" for item in res["results"]
    ]  # Likely need to update this

    async with aiohttp.ClientSession() as session:
        data_list = await fetch_all(session, urls)
        documents = [ExampleDB(**item) for item in data_list]
    print("Complete.")

    print("Adding documents...", end="")
    try:
        await ExampleDB.insert_many(documents)
        print("Complete.")
    except HTTPException:
        raise HTTPException(status_code=400, detail="Item could not be created.")


if __name__ == "__main__":
    asyncio.run(add_data())
