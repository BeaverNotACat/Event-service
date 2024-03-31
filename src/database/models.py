import uuid
from datetime import datetime
from typing import List

from sqlalchemy import Column, ForeignKey, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, relationship, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs

from src.database.file_storage import FileType


class Base(
    AsyncAttrs, DeclarativeBase
): ...  # In future here wil be timestamps and other data analisys shit


class Event(Base):
    __tablename__ = "event"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column()
    about: Mapped[str] = mapped_column()
    banner = Column(FileType())
    registration_start: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    registration_end: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    participation_start: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    participation_end: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    place_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("place.id"))
    target_group_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("target_group.id"))
    author_id: Mapped[uuid.UUID] = mapped_column()

    sport_type_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("sport_type.id"))
    place: Mapped["Place"] = relationship()
    social_links: Mapped[list["SocialLink"]] = relationship()
    sport_type: Mapped["SportType"] = relationship()
    starter_items: Mapped[List["StarterItem"]] = relationship()
    articles: Mapped[List["Article"]] = relationship()
    target_group: Mapped["TargetGroup"] = relationship()
    tickets: Mapped[list["Ticket"]] = relationship()
    documents: Mapped[List["Document"]] = relationship()


class Document(Base):
    __tablename__ = "document"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    event_id: Mapped[uuid.UUID] = mapped_column(ForeignKey(Event.id))
    file: Mapped[str] = mapped_column()
    name: Mapped[str] = mapped_column()


class Place(Base):
    __tablename__ = "place"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    country_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("country.id"))
    address: Mapped[str] = mapped_column()

    country: Mapped["Country"] = relationship()


class Country(Base):
    __tablename__ = "country"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(unique=True)


class SportType(Base):
    __tablename__ = "sport_type"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str] = mapped_column()


class TargetGroup(Base):
    __tablename__ = "target_group"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    gender: Mapped[str] = mapped_column()
    minimal_age: Mapped[int] = mapped_column()


class SocialLink(Base):
    __tablename__ = "social_link"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    event_id: Mapped[uuid.UUID] = mapped_column(ForeignKey(Event.id))
    link: Mapped[str] = mapped_column()


class Ticket(Base):
    __tablename__ = "ticket"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    event_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("event.id"))
    title: Mapped[str] = mapped_column()
    extra_title: Mapped[str] = mapped_column()
    price: Mapped[int] = mapped_column(nullable=True)
    max_places: Mapped[int] = mapped_column()
    sport_type_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("sport_type.id"))

    sport_type: Mapped["SportType"] = relationship()
    ticket_registrations: Mapped[list["TicketRegistration"]] = relationship()


class TicketRegistration(Base):
    __tablename__ = "ticket_registation"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    ticket_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("ticket.id"))
    user_id: Mapped[uuid.UUID] = mapped_column()
    serial_number: Mapped[int] = mapped_column()


class StarterItem(Base):
    __tablename__ = "starter_item"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    event_id: Mapped[uuid.UUID] = mapped_column(ForeignKey(Event.id))
    starter_item: Mapped[str] = mapped_column()


class Article(Base):
    __tablename__ = "article"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    event_id: Mapped[uuid.UUID] = mapped_column(ForeignKey(Event.id))
    title: Mapped[str] = mapped_column()
    text: Mapped[str] = mapped_column()
