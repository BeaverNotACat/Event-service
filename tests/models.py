from datetime import datetime
import uuid

from src.database.models import ( 
    Event,
    EventTranslation
)


def check_event_translations():
    ru = EventTranslation(
        title = "Хуй",
        about = "Хуй хуй",
        address = "Х. хуй",
        banner = "Хуй",
    )
    en = EventTranslation(
        title = "Dikc",
        about = "Dick dick",
        address = "D. dick",
        banner = "Dick",
    )
    event = Event(
        registration_start = datetime.utcnow(),
        registration_end = datetime.utcnow(),
        participation_start = datetime.utcnow(),
        participation_end = datetime.utcnow(),
        sport_type_id = uuid.uuid4(),
        organizer_id = uuid.uuid4()
    )

    event.translations["en-US"] = en
    event.translations["ru-RU"] = ru

    assert event.translations["ru-RU"] == ru
    assert event.translations["en-US"] == en


if __name__ == "__main__":
    check_event_translations()
