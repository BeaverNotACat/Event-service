import uuid
from datetime import datetime
from typing import List

from sqlalchemy import ForeignKey, DateTime, String, UniqueConstraint, inspect
from sqlalchemy.orm import DeclarativeBase, Mapped, relationship, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy_utils.types.currency import CurrencyType


class Base(AsyncAttrs, DeclarativeBase):
    # In future here wil be timestamps and other data analisys shit
    def to_dict(self):
        """
        Method for parsinng expired and detached from session models.
        E.g. when pydantic serialize output
        THIS SHIT WAS BROCKEN FUCK YOU TIANGOLO
        """
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}


class Event(Base):
    __tablename__ = "event"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    registration_start: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    registration_end: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    participation_start: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    participation_end: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    minimal_age: Mapped[int] = mapped_column()
    sport_type_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("sport_type.id"))
    organizer_id: Mapped[uuid.UUID] = mapped_column()

    social_links: Mapped[list["SocialLink"]] = relationship()
    sport_type: Mapped["SportType"] = relationship()
    tickets: Mapped[list["Ticket"]] = relationship()
    documents: Mapped[list["Document"]] = relationship()

    localisations: Mapped[list["EventLocalisation"]] = relationship()


class EventLocalisation(Base):
    __tablename__ = "event_localisation"
    id: Mapped[uuid.UUID] = mapped_column(default=uuid.uuid4, primary_key=True)
    event_id: Mapped[uuid.UUID] = mapped_column(ForeignKey(Event.id))
    language_code: Mapped[str] = mapped_column(String(5))  # BCP 47

    title: Mapped[str] = mapped_column()
    about: Mapped[str] = mapped_column()
    address: Mapped[str] = mapped_column()
    banner_filename: Mapped[str] = mapped_column(default="default.png")
    articles: Mapped[List["Article"]] = relationship()
    starter_items: Mapped[List["StarterItem"]] = relationship()

    UniqueConstraint(event_id, language_code)


class SportType(Base):
    __tablename__ = "sport_type"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    localisations: Mapped[list["SportTypeLocalisation"]] = relationship()


class SportTypeLocalisation(Base):
    __tablename__ = "sport_type_translation"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    sport_type_id: Mapped[uuid.UUID] = mapped_column(ForeignKey(SportType.id))
    language_code: Mapped[str] = mapped_column(String(5))  # BCP 47
    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str] = mapped_column()


class Document(Base):
    __tablename__ = "document"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    event_id: Mapped[uuid.UUID] = mapped_column(ForeignKey(Event.id))
    title: Mapped[str] = mapped_column()
    filename: Mapped[str] = mapped_column()


class SocialLink(Base):
    __tablename__ = "social_link"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    event_id: Mapped[uuid.UUID] = mapped_column(ForeignKey(Event.id))
    link: Mapped[str] = mapped_column()


class StarterItem(Base):
    __tablename__ = "starter_item"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    event_translation_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey(EventLocalisation.id)
    )
    name: Mapped[str] = mapped_column()


class Article(Base):
    __tablename__ = "article"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    event_translation_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey(EventLocalisation.id)
    )
    title: Mapped[str] = mapped_column()
    text: Mapped[str] = mapped_column()


class Ticket(Base):
    __tablename__ = "ticket"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    event_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("event.id"))
    max_places: Mapped[int] = mapped_column()
    sport_type_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("sport_type.id"))

    sport_type: Mapped["SportType"] = relationship()
    registrations: Mapped[list["TicketRegistration"]] = relationship()


class TicketLocalisation(Base):
    __tablename__ = "ticket_translation"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    ticket_id: Mapped[uuid.UUID] = mapped_column(ForeignKey(SportType.id))
    language_code: Mapped[str] = mapped_column(String(5))  # BCP 47
    title: Mapped[str] = mapped_column()
    extra_title: Mapped[str] = mapped_column()
    price = mapped_column(CurrencyType, nullable=True)


class TicketRegistration(Base):
    __tablename__ = "ticket_registation"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    ticket_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("ticket.id"))
    user_id: Mapped[uuid.UUID] = mapped_column()
    serial_number: Mapped[int] = mapped_column()
