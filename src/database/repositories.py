import typing

from src.database.models import (
    Event,
    EventTranslation,
    Ticket,
    TicketTranslation,
    SportType,
    SportTypeTranslation,
    Document,
    SocialLink,
    StarterItem,
    Article,
    TicketRegistration,
)
from src.utils.repository import SQLAlchemyRepository


class EventRepository(SQLAlchemyRepository):
    model = Event


class EventTranslationRepository(SQLAlchemyRepository):
    model = EventTranslation


class TicketRepository(SQLAlchemyRepository):
    model = Ticket


class TicketTranslationRepository(SQLAlchemyRepository):
    model = TicketTranslation


class SportTypeRepository(SQLAlchemyRepository):
    model = SportType


class SportTypeTranslationRepository(SQLAlchemyRepository):
    model = SportTypeTranslation


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


