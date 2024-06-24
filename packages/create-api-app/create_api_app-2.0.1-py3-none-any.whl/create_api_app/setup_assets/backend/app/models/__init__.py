from typing import Optional

from app.config.settings import settings

from beanie import Document
from pydantic import BaseModel


class ExampleDB(Document):
    """The main model for database collection based on the database."""

    name: str
    desc: Optional[str] = None

    class Settings:
        name = settings.DB_COLLECTION_NAME


__beanie_models__ = [ExampleDB]
