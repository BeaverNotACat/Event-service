from abc import ABC, abstractmethod

from src.database.session import async_session_maker
from src.database.repositories import (
    EventRepository,
    EventLocalisationRepository,
    SportTypeRepository,
    TicketRepository,
    TicketLocalisationRepository,
    TicketRegistrationRepository,
    SportTypeLocalisationRepository,
    DocumentRepository,
    SocialLinkRepository,
    StarterItemRepository,
    ArticleRepository,
)


class IUnitOfWork(ABC):
    event: EventRepository
    event_localisation: EventLocalisationRepository
    sport_type: SportTypeRepository
    sport_type_localisation: SportTypeLocalisationRepository
    ticket: TicketRepository
    ticket_localisation: TicketLocalisationRepository
    ticket_registration: TicketRegistrationRepository
    document: DocumentRepository
    social_link: SocialLinkRepository
    starter_item: StarterItemRepository
    article: ArticleRepository

    @abstractmethod
    def __init__(self): ...

    @abstractmethod
    async def __aenter__(self): ...

    @abstractmethod
    async def __aexit__(self, *args): ...

    @abstractmethod
    async def commit(self): ...

    @abstractmethod
    async def rollback(self): ...


class UnitOfWork(IUnitOfWork):
    def __init__(self):
        self.db_session_factory = async_session_maker

    async def __aenter__(self):
        self.db_session = self.db_session_factory()

        self.event = EventRepository(self.db_session)
        self.event_localisation = EventLocalisationRepository(self.db_session)
        self.sport_type = SportTypeRepository(self.db_session)
        self.sport_type_localisation = SportTypeLocalisationRepository(self.db_session)
        self.ticket = TicketRepository(self.db_session)
        self.ticket_localisation = TicketLocalisationRepository(self.db_session)
        self.ticket_registration = TicketRegistrationRepository(self.db_session)
        self.social_link = SocialLinkRepository(self.db_session)
        self.starter_item = StarterItemRepository(self.db_session)
        self.article = ArticleRepository(self.db_session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.db_session.close()

    async def commit(self):
        await self.db_session.commit()

    async def rollback(self):
        await self.db_session.rollback()
