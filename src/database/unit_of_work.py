from abc import ABC, abstractmethod

from src.database.s3_storage import s3_session_maker
from src.database.session import async_session_maker
from src.database.repositories import (
    EventRepository,
    EventLocalizationRepository,
    SportRepository,
    TicketRepository,
    TicketLocalizationRepository,
    TicketRegistrationRepository,
    SportLocalizationRepository,
    DocumentRepository,
    SocialLinkRepository,
    StarterItemRepository,
    ArticleRepository,
)
from src.utils.repository import S3Repository


class IUnitOfWork(ABC):
    s3: S3Repository
    event: EventRepository
    event_localization: EventLocalizationRepository
    sport: SportRepository
    sport_localization: SportLocalizationRepository
    ticket: TicketRepository
    ticket_localization: TicketLocalizationRepository
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
        self.s3_session_factory = s3_session_maker

    async def __aenter__(self):
        self.db_session = self.db_session_factory()
        self.s3_session = self.s3_session_factory()

        self.s3 = S3Repository(self.s3_session)
        self.event = EventRepository(self.db_session)
        self.event_localization = EventLocalizationRepository(self.db_session)
        self.sport = SportRepository(self.db_session)
        self.sport_localization = SportLocalizationRepository(self.db_session)
        self.ticket = TicketRepository(self.db_session)
        self.ticket_localization = TicketLocalizationRepository(self.db_session)
        self.ticket_registration = TicketRegistrationRepository(self.db_session)
        self.social_link = SocialLinkRepository(self.db_session)
        self.starter_item = StarterItemRepository(self.db_session)
        self.article = ArticleRepository(self.db_session)
        self.document = DocumentRepository(self.db_session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.db_session.close()

    async def commit(self):
        await self.db_session.commit()

    async def rollback(self):
        await self.db_session.rollback()
