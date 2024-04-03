import uuid
import typing
from datetime import datetime

from pydantic import BaseModel
from sqlalchemy_utils.types.currency import Currency


class EventPydantic(BaseModel):
    id: typing.Optional[uuid.UUID]
    organizer_id: uuid.UUID
    spotr_type_id: typing.Optional[uuid.UUID]
    regidstration_start: datetime
    regidstration_end: datetime
    participation_start: datetime
    participation_end: datetime
    minimal_age: int
    sport_type: typing.Optional["SportTypePydantic"]
    social_links: list["SocialLinkPydantic"]
    tickets: list["TicketPydantic"]
    documents: list["DocumentPydantic"]
    translations: dict[str, "EventTranslationPydantic"]
        

class EventTranslationPydantic(BaseModel):
    id: typing.Optional[uuid.UUID]
    title: str
    about: str
    address: str
    banner_filename: str
    atricles: list["ArticlePydantic"]
    starter_items: list["StarterItemPydantic"]


class DocumentPydantic(BaseModel):
    id: typing.Optional[uuid.UUID]
    title: str
    filename: str
    

class SportTypePydantic(BaseModel):
    id: typing.Optional[uuid.UUID]
    translations: dict[str, "SportTypeTranslationPydantic"]


class SportTypeTranslationPydantic(BaseModel):
    id: typing.Optional[uuid.UUID]
    event_id: typing.Optional[uuid.UUID]
    name: str
    description: str


class SocialLinkPydantic(BaseModel):
    id: typing.Optional[uuid.UUID]
    event_id: typing.Optional[uuid.UUID]
    link: str


class StarterItemPydantic(BaseModel):
    id: typing.Optional[uuid.UUID]
    event_translation_id: typing.Optional[uuid.UUID]
    name: str


class ArticlePydantic(BaseModel):
    id: typing.Optional[uuid.UUID]
    event_translation_id: typing.Optional[uuid.UUID]
    title: str
    text: str


class TicketPydantic(BaseModel):
    id: typing.Optional[uuid.UUID]
    event_id: typing.Optional[uuid.UUID]
    spotr_type_id: typing.Optional[uuid.UUID]
    max_places: int
    sport_type: typing.Optional[SportTypePydantic]
    registrations: list["TicketRegistrationsPydantic"]
    translations: dict[str, "TicketTranslationPydantic"]


class TicketTranslationPydantic(BaseModel):
    id: typing.Optional[uuid.UUID]
    title: str
    extra_title: str
    price: Currency


class TicketRegistrationsPydantic(BaseModel):
    id: typing.Optional[uuid.UUID]
    ticket_id: typing.Optional[uuid.UUID]
    user_id: typing.Optional[uuid.UUID]
    serial_number: int
