from src.database.models import (
    Address,
    Event,
    Article,
    EventLocalization,
    Sport,
    SportLocalization,
    StarterItem,
)
from src.schemas.schemas import CreateEvent, CreateSport


def event_schema_to_model(event_schema: CreateEvent) -> Event:
    event_model = Event(
        registration_start_at=event_schema.registration_start_at,
        registration_end_at=event_schema.registration_end_at,
        participation_start_at=event_schema.participation_start_at,
        participation_end_at=event_schema.participation_end_at,
        minimal_age=event_schema.minimal_age,
        sport_id=event_schema.sport_id,
        organizer_id=event_schema.organizer_id,  # TODO remake with tockens
    )
    for key in event_schema.localizations:
        localization = event_schema.localizations[key]
        event_model.localizations[key] = EventLocalization(
            title=localization.title,
            about=localization.about,
            articles=[
                Article(**schema.model_dump()) for schema in localization.articles
            ],
            address=Address(**localization.address.model_dump()),
            starter_items=[
                StarterItem(**schema.model_dump())
                for schema in localization.starter_items
            ],
        )

    return event_model


def sport_schema_to_model(sport_schema: CreateSport) -> Sport:
    sport_model = Sport()
    for key in sport_schema.localizations:
        localization = sport_schema.localizations[key]
        sport_model.localizations[key] = SportLocalization(
            name=localization.name,
            description=localization.description,
        )
    return sport_model
