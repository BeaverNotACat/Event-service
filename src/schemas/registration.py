import uuid
from typing import Optional

from pydantic import BaseModel
from pydantic_core.core_schema import DateSchema


class RegistrationSchema(BaseModel):
    ticket_id: uuid.UUID
    user_id: uuid.UUID


class GetRegistrationsSchema(BaseModel):
    user_id: uuid.UUID


class GetEventParticipants(BaseModel):
    name: str
    second_name: str
    serial_number: str
    club: Optional[str]
    date_of_birth: DateSchema


class PostRegister(BaseModel):
    ticket_id: uuid.UUID
