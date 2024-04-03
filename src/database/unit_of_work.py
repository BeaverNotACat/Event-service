from abc import ABC, abstractmethod

from src.database.session import async_session_maker
from src.database.repositories import (
    EventRepository,
    EventTranslationRepository,
    SportTypeRepository,
    TicketRepository,
    TicketTranslationRepository,
    TicketRegistrationRepository,
    SportTypeTranslationRepository,
    DocumentRepository,
    SocialLinkRepository,
    StarterItemRepository,
    ArticleRepository,
)

class IUnitOfWork(ABC):
    event: EventRepository
    event_translation: EventTranslationRepository
    sport_type: SportTypeRepository
    sport_type_translation: SportTypeTranslationRepository
    ticket: TicketRepository
    ticket_translation: TicketTranslationRepository
    ticket_registration: TicketRegistrationRepository
    document: DocumentRepository
    social_link: SocialLinkRepository
    starter_item: StarterItemRepository
    article: ArticleRepository

    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    async def __aenter__(self):
        ...

    @abstractmethod
    async def __aexit__(self, *args):
        ...

    @abstractmethod
    async def commit(self):
        ...

    @abstractmethod
    async def rollback(self):
        ...


class UnitOfWork:
    def __init__(self):
        self.session_factory = async_session_maker

    async def __aenter__(self):
        self.session = self.session_factory()

        self.event = EventRepository(self.session)
        self.event_translation = EventTranslationRepository(self.session)
        self.sport_type = SportTypeRepository(self.session)
        self.sport_type_translation = EventTranslationRepository(self.session)
        self.ticket = TicketRepository(self.session)
        self.ticket_translation = TicketTranslationRepository(self.session)
        self.ticket_registration = TicketRegistrationRepository(self.session)
        self.social_link = SocialLinkRepository(self.session)
        self.starter_item = StarterItemRepository(self.session)
        self.article = ArticleRepository(self.session)
        
    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
