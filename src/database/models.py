import uuid
from datetime import datetime
from typing import List

from sqlalchemy import ForeignKey, DateTime, String
from sqlalchemy.orm import DeclarativeBase, Mapped, relationship, mapped_column
from sqlalchemy.orm.collections import attribute_keyed_dict
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.associationproxy import AssociationProxy
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy_utils.types.currency import CurrencyType


class Base(
    AsyncAttrs, DeclarativeBase
): ...  # In future here wil be timestamps and other data analisys shit


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
    documents: Mapped[List["Document"]] = relationship()
    translation_associations: Mapped[dict[str, "EventTranslationAssociation"]] = (
        relationship(
            back_populates="event",
            collection_class=attribute_keyed_dict("language_code"),
            cascade="all, delete-orphan",
        )
    )
    translations: AssociationProxy[dict[str, "EventTranslation"]] = association_proxy(
        "translation_associations",
        "translation",
        creator=lambda k, v: EventTranslationAssociation(
            language_code=k, translation=v
        ),
    )


class EventTranslationAssociation(Base):
    """Many to many relationship that provides dictionary proxy"""

    __tablename__ = "event_traslation_association"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    event_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("event.id"), primary_key=True
    )
    event_translation_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("event_translation.id"), primary_key=True
    )
    language_code: Mapped[str] = mapped_column(String(5))  # BCP 47

    event: Mapped[Event] = relationship(back_populates="translation_associations")
    translation: Mapped["EventTranslation"] = relationship()


class EventTranslation(Base):
    __tablename__ = "event_translation"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column()
    about: Mapped[str] = mapped_column()
    address: Mapped[str] = mapped_column()
    banner_filename: Mapped[str] = mapped_column()
    articles: Mapped[List["Article"]] = relationship()
    starter_items: Mapped[List["StarterItem"]] = relationship()


class SportType(Base):
    __tablename__ = "sport_type"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    translation_associations: Mapped[dict[str, "SportTypeTranslationAssociation"]] = (
        relationship(
            back_populates="sport_type",
            collection_class=attribute_keyed_dict("language_code"),
            cascade="all, delete-orphan",
        )
    )
    translations: AssociationProxy[dict[str, "SportTypeTranslation"]] = association_proxy(
        "translation_associations",
        "translation",
        creator=lambda k, v: SportTypeTranslationAssociation(
            language_code=k, translation=v
        ),
    )


class SportTypeTranslationAssociation(Base):
    __tablename__ = "sport_type_translation_association"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    sport_type_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("sport_type.id"), primary_key=True
    )
    sport_type_translation_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("sport_type_translation.id"), primary_key=True
    )
    language_code: Mapped[str] = mapped_column(String(5))  # BCP 47

    sport_type: Mapped[SportType] = relationship(back_populates="translation_associations")
    translation: Mapped["SportTypeTranslation"] = relationship()


class SportTypeTranslation(Base):
    __tablename__ = "sport_type_translation"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
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
    event_translation_id: Mapped[uuid.UUID] = mapped_column(ForeignKey(EventTranslation.id))
    name: Mapped[str] = mapped_column()


class Article(Base):
    __tablename__ = "article"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    event_translation_id: Mapped[uuid.UUID] = mapped_column(ForeignKey(EventTranslation.id))
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
    translation_associations: Mapped[dict[str, "TicketTranslationAssociation"]] = (
        relationship(
            back_populates="ticket",
            collection_class=attribute_keyed_dict("language_code"),
            cascade="all, delete-orphan",
        )
    )
    translations: AssociationProxy[dict[str, "TicketTranslation"]] = association_proxy(
        "translation_associations",
        "translation",
        creator=lambda k, v: SportTypeTranslationAssociation(
            language_code=k, translation=v
        ),
    )


class TicketTranslationAssociation(Base):
    __tablename__ = "ticket_translation_assiciation"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    ticket_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("ticket.id"), primary_key=True
    )
    ticket_translation_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("ticket_translation.id"), primary_key=True
    )
    language_code: Mapped[str] = mapped_column(String(5))  # BCP 47

    ticket: Mapped[Ticket] = relationship(back_populates="translation_associations")
    translation: Mapped["TicketTranslation"] = relationship()


class TicketTranslation(Base):
    __tablename__ = "ticket_translation"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column()
    extra_title: Mapped[str] = mapped_column()
    price = mapped_column(CurrencyType, nullable=True)


class TicketRegistration(Base):
    __tablename__ = "ticket_registation"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    ticket_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("ticket.id"))
    user_id: Mapped[uuid.UUID] = mapped_column()
    serial_number: Mapped[int] = mapped_column()
