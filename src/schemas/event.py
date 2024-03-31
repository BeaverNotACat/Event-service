import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class EventListFilterSchema(BaseModel):
    search: Optional[str] = None
    sport_type: Optional[uuid.UUID] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    is_avaliable: Optional[bool] = None


class GetEventList(BaseModel):
    id: uuid.UUID
    banner: Optional[str]
    title: str
    place: "PlaceSchema"
    tickets: list["TicketSchema"]
    participation_start: datetime
    participation_end: datetime
    sport_type: "SportTypeSchema"


class GetEvent(GetEventList):
    about: str
    starter_items: list["StarterItemsSchema"]
    articles: list["ArticleSchema"]
    documents: Optional[list["DocumentSchema"]]
    registration_start: datetime
    registration_end: datetime
    social_links: list["SocialLinkSchema"]
    sport_type: "SportTypeSchema"


class SocialLinkSchema(BaseModel):
    link: str


class SportTypeSchema(BaseModel):
    id: uuid.UUID
    name: str
    description: str


class SportTypeNameSchema(BaseModel):
    name: str


class DocumentSchema(BaseModel):
    file: str
    name: str


class PlaceSchema(BaseModel):
    country: "CountrySchema"
    address: str


class CountrySchema(BaseModel):
    name: str


class TargetGroupSchema(BaseModel):
    gender: str
    minimal_age: int


class TicketSchema(BaseModel):
    id: uuid.UUID
    title: str
    extra_title: str
    price: int
    max_places: int
    sport_type: "SportTypeNameSchema"


class StarterItemsSchema(BaseModel):
    starter_item: str


class ArticleSchema(BaseModel):
    title: str
    text: str
