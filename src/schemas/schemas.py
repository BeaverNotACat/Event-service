import uuid
from enum import StrEnum
from datetime import datetime

from pydantic import BaseModel, RootModel, ConfigDict, computed_field

from src.database.s3_storage import s3_session_maker


class LanguageCode(StrEnum):
    en = "en"
    ru = "ru"
    cn = "cn"


class CreateEvent(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    registration_start_at: datetime
    registration_end_at: datetime
    participation_start_at: datetime
    participation_end_at: datetime
    minimal_age: int
    sport_id: uuid.UUID
    organizer_id: uuid.UUID  # TODO remake with tockens
    localizations: dict[LanguageCode, "CreateEventLocalization"]


class GetEvent(CreateEvent):
    model_config = ConfigDict(from_attributes=True)
    id: uuid.UUID
    documents: list["GetDocument"]
    localizations: dict[LanguageCode, "GetEventLocalization"]


class GetEventList(RootModel):
    model_config = ConfigDict(from_attributes=True)
    root: list[GetEvent]


class CreateEventLocalization(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str
    about: str
    articles: list["CreateArticle"]
    address: "CreateAddress"


class GetEventLocalization(CreateEventLocalization):
    banner_filename: str

    @computed_field
    def banner_filepath(self) -> str:
        return s3_session_maker().get_path(self.banner_filename)


class CreateArticle(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str
    text: str


class CreateAddress(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    postal_code: str
    country: str
    state: str
    city: str
    line: str


class CreateStarterItem(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str


class CreateSport(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    localizations: dict[LanguageCode, "CreateSportLocalization"]


class GetSport(CreateSport):
    model_config = ConfigDict(from_attributes=True)
    id: uuid.UUID


class GetSportList(RootModel):
    model_config = ConfigDict(from_attributes=True)
    root: list[GetSport]


class CreateSportLocalization(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    description: str


class CreateDocument(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str


class GetDocument(CreateDocument):
    model_config = ConfigDict(from_attributes=True)
    filename: str

    @computed_field
    def filepath(self) -> str:
        return s3_session_maker().get_path(self.filename)
