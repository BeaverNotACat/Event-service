from sqlalchemy import select

from src.database.models import (
    Event,
    EventLocalisation,
    Ticket,
    TicketLocalisation,
    SportType,
    SportTypeLocalisation,
    Document,
    SocialLink,
    StarterItem,
    Article,
    TicketRegistration,
)
from src.utils.repository import SQLAlchemyRepository


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
        return res.scalars().fetchall()


class EventLocalisationRepository(SQLAlchemyRepository):
    model = EventLocalisation


class TicketRepository(SQLAlchemyRepository):
    model = Ticket


class TicketLocalisationRepository(SQLAlchemyRepository):
    model = TicketLocalisation


class SportTypeRepository(SQLAlchemyRepository):
    model = SportType


class SportTypeLocalisationRepository(SQLAlchemyRepository):
    model = SportTypeLocalisation


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
