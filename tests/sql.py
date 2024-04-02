import io
import asyncio
from datetime import datetime
import uuid

from fastapi import UploadFile

from src.database.session import async_session_maker
from src.database.models import Event, EventTranslation, SportType


async def test_file_creation():
    event = Event(
        registration_start = datetime.utcnow(),
        registration_end = datetime.utcnow(),
        participation_start = datetime.utcnow(),
        participation_end = datetime.utcnow(),
        sport_type_id = (sport_id := uuid.uuid4()),
        organizer_id = uuid.uuid4(),
        minimal_age = 18,
    )
    ru = EventTranslation(
        title = "Хуй",
        about = "Хуй хуй",
        address = "Х. хуй",
        banner = UploadFile(
            file=io.BytesIO(b"some initial text data"),
            filename='banner.jpg'
        )
    )
    en = EventTranslation(
        title = "Dikc",
        about = "Dick dick",
        address = "D. dick",
        banner = UploadFile(
            file=io.BytesIO(b"some initial text data"),
            filename='banner.jpg'
        )
    )
    event.translations["en-US"] = en
    event.translations["ru-RU"] = ru

    sport = SportType(id = sport_id)

    async with async_session_maker() as session:
        session.add(sport)
        session.add(event)
        await session.commit()

if __name__ == '__main__':   
    asyncio.run(test_file_creation())
