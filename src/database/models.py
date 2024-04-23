import uuid
from datetime import datetime
from typing import List

from sqlalchemy import ForeignKey, DateTime, String, UniqueConstraint
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    relationship,
    mapped_column,
)
from sqlalchemy.orm.collections import attribute_keyed_dict
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.associationproxy import AssociationProxy
from sqlalchemy.ext.asyncio import AsyncAttrs


class Base(
    AsyncAttrs, DeclarativeBase
): ...  # In future here wil be timestamps and other data analisys shit


class Sport(Base):
    __tablename__ = "sport"
    __mapper_args__ = {"eager_defaults": True}
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    localization_associations: Mapped[dict[str, "SportLocalizationAssociation"]] = (
        relationship(
            back_populates="sport",
            collection_class=attribute_keyed_dict("language"),
            cascade="all, delete-orphan",
            lazy="joined",
        )
    )
    localizations: AssociationProxy[dict[str, "SportLocalization"]] = association_proxy(
        "localization_associations",
        "localization",
        creator=lambda k, v: SportLocalizationAssociation(language=k, localization=v),
    )


class SportLocalization(Base):
    __tablename__ = "sport_localization"
    __mapper_args__ = {"eager_defaults": True}
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()


class SportLocalizationAssociation(Base):
    __tablename__ = "sport_localization_association"
    __mapper_args__ = {"eager_defaults": True}
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    sport_id: Mapped[uuid.UUID] = mapped_column(ForeignKey(Sport.id), primary_key=True)
    sport_localization_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey(SportLocalization.id), primary_key=True
    )
    language: Mapped[str] = mapped_column(String(2))

    sport: Mapped[Sport] = relationship(
        back_populates="localization_associations", lazy="joined"
    )
    localization: Mapped["SportLocalization"] = relationship(lazy="joined")


class Event(Base):
    __tablename__ = "event"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    registration_start_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    registration_end_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    participation_start_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    participation_end_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    minimal_age: Mapped[int] = mapped_column()
    sport_id: Mapped[uuid.UUID] = mapped_column(ForeignKey(Sport.id))
    organizer_id: Mapped[uuid.UUID] = mapped_column()

    social_links: Mapped[list["SocialLink"]] = relationship(lazy="joined")
    sport: Mapped["Sport"] = relationship(lazy="joined")
    tickets: Mapped[list["Ticket"]] = relationship(lazy="joined")
    documents: Mapped[List["Document"]] = relationship(lazy="joined")
    localization_associations: Mapped[dict[str, "EventLocalizationAssociation"]] = (
        relationship(
            back_populates="event",
            collection_class=attribute_keyed_dict("language"),
            cascade="all, delete-orphan",
            lazy="joined",
        )
    )
    localizations: AssociationProxy[dict[str, "EventLocalization"]] = association_proxy(
        "localization_associations",
        "localization",
        creator=lambda k, v: EventLocalizationAssociation(language=k, localization=v),
    )


class EventLocalization(Base):
    __tablename__ = "event_localization"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)

    title: Mapped[str] = mapped_column()
    about: Mapped[str] = mapped_column()
    banner_filename: Mapped[str] = mapped_column(default="default.png")
    articles: Mapped[List["Article"]] = relationship(
        lazy="joined",
    )
    starter_items: Mapped[List["StarterItem"]] = relationship(
        lazy="joined",
    )
    address: Mapped["Address"] = relationship(
        lazy="joined",
    )


class EventLocalizationAssociation(Base):
    """Many to many relationship that provides dictionary proxy"""

    __tablename__ = "event_traslation_association"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    event_id: Mapped[uuid.UUID] = mapped_column(ForeignKey(Event.id), primary_key=True)
    event_localization_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey(EventLocalization.id), primary_key=True
    )
    language: Mapped[str] = mapped_column(String(2))

    event: Mapped[Event] = relationship(
        back_populates="localization_associations", lazy="joined"
    )
    localization: Mapped["EventLocalization"] = relationship(lazy="joined")


class Address(Base):
    __tablename__ = "address"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    event_localization_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey(EventLocalization.id), unique=True
    )

    postal_code: Mapped[str] = mapped_column()
    country: Mapped[str] = mapped_column(String(2))
    state: Mapped[str] = mapped_column()
    city: Mapped[str] = mapped_column()
    line: Mapped[str] = mapped_column()


class Document(Base):
    __tablename__ = "document"
    __table_args__ = (UniqueConstraint("event_id", "title"),)
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
    event_localization_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey(EventLocalization.id)
    )

    name: Mapped[str] = mapped_column()


class Article(Base):
    __tablename__ = "article"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    event_localization_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey(EventLocalization.id)
    )

    title: Mapped[str] = mapped_column()
    text: Mapped[str] = mapped_column()


class Money(Base):
    __tablename__ = "money"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    amount: Mapped[float] = mapped_column()
    currency: Mapped[str] = mapped_column(String(3))


class Ticket(Base):
    __tablename__ = "ticket"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    event_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("event.id"))

    max_places: Mapped[int] = mapped_column()
    # sport: Mapped["Sport"] = relationship()
    registrations: Mapped[list["TicketRegistration"]] = relationship()
    localization_associations: Mapped[dict[str, "TicketlocalizationAssociation"]] = (
        relationship(
            back_populates="ticket",
            collection_class=attribute_keyed_dict("language"),
            cascade="all, delete-orphan",
        )
    )
    localizations: AssociationProxy[dict[str, "TicketLocalization"]] = (
        association_proxy(
            "localization_associations",
            "localization",
            creator=lambda k, v: SportLocalizationAssociation(
                language=k, localization=v
            ),
        )
    )


class TicketlocalizationAssociation(Base):
    __tablename__ = "ticket_localization_assiciation"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    ticket_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("ticket.id"), primary_key=True
    )
    ticket_localization_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("ticket_localization.id"), primary_key=True
    )
    language: Mapped[str] = mapped_column(String(2))  # BCP 47

    ticket: Mapped[Ticket] = relationship(back_populates="localization_associations")
    localization: Mapped["TicketLocalization"] = relationship()


class TicketLocalization(Base):
    __tablename__ = "ticket_localization"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column()
    extra_title: Mapped[str] = mapped_column()
    price_id: Mapped[uuid.UUID] = mapped_column(ForeignKey(Money.id))
    price: Mapped["Money"] = relationship()


class TicketRegistration(Base):
    __tablename__ = "ticket_registation"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    ticket_id: Mapped[uuid.UUID] = mapped_column(ForeignKey(Ticket.id))
    user_id: Mapped[uuid.UUID] = mapped_column()
    serial_number: Mapped[int] = mapped_column()
