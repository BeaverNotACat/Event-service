import uuid
import typing
from enum import StrEnum
from datetime import datetime

from pydantic import RootModel

from src.utils.schemas import ConfiguredBaseModel


class LanguageCode(StrEnum):
    en = "EN_US"
    ru = "RU_RU"


class GetEvent(ConfiguredBaseModel):
    id: uuid.UUID
    registration_start: datetime
    registration_end: datetime
    participation_start: datetime
    participation_end: datetime
    minimal_age: int
    sport_type_id: uuid.UUID
    organizer_id: uuid.UUID

    # social_links: list["GetSocialLink"]
    # sport_type: "SportType"
    # tickets: list["Ticket"]
    # documents: list["Document"]


class GetEventList(RootModel):
    root: list[GetEvent]


class CreateEvent(ConfiguredBaseModel):
    organizer_id: uuid.UUID  # TODO Remake with authorization
    registration_start: datetime
    registration_end: datetime
    participation_start: datetime
    participation_end: datetime
    minimal_age: int

    sport_type_id: typing.Optional[uuid.UUID]


class GetEventLocalisation(ConfiguredBaseModel):
    event_id: uuid.UUID
    language_code: LanguageCode

    title: str
    about: str
    address: str


class GetEventLocalisationList(RootModel):
    root: list[GetEventLocalisation]


class CreateEventLocalisation(ConfiguredBaseModel):
    title: str
    about: str
    address: str


class CreateStarterItem(ConfiguredBaseModel):
    event_translation_id: uuid.UUID

    name: str


class CreateDocumentPydantic(ConfiguredBaseModel):
    event_id: uuid.UUID

    title: str
    filename: str


class CreateSportTypePydantic(ConfiguredBaseModel): ...


class CreateSportTypeTranslationPydantic(ConfiguredBaseModel):
    sport_type_id: uuid.UUID

    name: str
    description: str


class SocialLinkPydantic(ConfiguredBaseModel):
    event_id: typing.Optional[uuid.UUID]

    link: str


class GetArticlePydantic(ConfiguredBaseModel):
    title: str
    text: str


class CreateArticlePydantic(ConfiguredBaseModel):
    title: str
    text: str


# class TicketPydantic(CondiguredBaseModel):
#     id: typing.Optional[uuid.UUID] = None
#     event_id: typing.Optional[uuid.UUID]
#     spotr_type_id: typing.Optional[uuid.UUID]
#     max_places: int
#     registrations: list["TicketRegistrationsPydantic"]
#     translations: dict[str, "TicketTranslationPydantic"]


# class TicketTranslationPydantic(CondiguredBaseModel):
#     id: typing.Optional[uuid.UUID] = None
#     title: str
#     extra_title: str
#     price: Currency


# class TicketRegistrationsPydantic(CondiguredBaseModel):
#     id: typing.Optional[uuid.UUID] = None
#     ticket_id: typing.Optional[uuid.UUID]
#     user_id: typing.Optional[uuid.UUID]
#     serial_number: int
