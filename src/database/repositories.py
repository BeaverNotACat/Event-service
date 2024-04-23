from sqlalchemy import select

from src.database.models import (
    Event,
    EventLocalization,
    Ticket,
    TicketLocalization,
    Sport,
    SportLocalization,
    Document,
    SocialLink,
    StarterItem,
    Article,
    TicketRegistration,
)
from src.schemas.schemas import CreateEvent, CreateSport
from src.utils.repository import SQLAlchemyRepository
from src.utils.mappers import event_schema_to_model, sport_schema_to_model


class EventRepository(SQLAlchemyRepository):
    model = Event

    async def find_all_paginated(self, limit: int, offset: int):
        stmt = (
            select(self.model)
            .options(*self.get_select_options())
            .limit(limit)
            .offset(offset)
        )  # type: ignore
        res = await self.session.execute(stmt)
        return res.unique().scalars().fetchall()

    async def add_one_schema(self, schema: CreateEvent) -> Event:
        model = event_schema_to_model(schema)
        self.session.add(model)
        return model


class EventLocalizationRepository(SQLAlchemyRepository):
    model = EventLocalization


class TicketRepository(SQLAlchemyRepository):
    model = Ticket


class TicketLocalizationRepository(SQLAlchemyRepository):
    model = TicketLocalization


class SportRepository(SQLAlchemyRepository):
    model = Sport

    async def add_one_schema(self, schema: CreateSport) -> Sport:
        model = sport_schema_to_model(schema)
        self.session.add(model)
        return model


class SportLocalizationRepository(SQLAlchemyRepository):
    model = SportLocalization


class DocumentRepository(SQLAlchemyRepository):
    model = Document


class SocialLinkRepository(SQLAlchemyRepository):
    model = SocialLink


class StarterItemRepository(SQLAlchemyRepository):
    model = StarterItem


class ArticleRepository(SQLAlchemyRepository):
    model = Article


class TicketRegistrationRepository(SQLAlchemyRepository):
    model = TicketRegistration
