import io
import asyncio
from datetime import datetime
import uuid

from fastapi import UploadFile
from src.database.session import async_session_maker
from src.database.s3_storage import get_storage
from src.database.models import Event, EventTranslation, SportType


async def test_file_creation():
    banner = UploadFile(
        file=io.BytesIO(b"some initial text data"),
        filename='banner.jpg',
    )
    banner_path = get_storage().write(banner.file, banner.filename)
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
        banner_filename=banner_path
    )
    en = EventTranslation(
        title = "Dikc",
        about = "Dick dick",
        address = "D. dick",
        banner_filename=banner_path
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
