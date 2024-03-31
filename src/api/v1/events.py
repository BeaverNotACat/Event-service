from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Header
from src.schemas.auth import UserProfileSchema

from src.schemas.event import (
    EventListFilterSchema,
    GetEvent,
    GetEventList,
    SportTypeSchema,
)
from src.schemas.registration import (
    PostRegister,
    RegistrationSchema,
)
from src.service.event import get_event_service
from src.service.registration import get_registraton_service
from src.service.sport_type import get_sport_type_service

events_router = APIRouter(
    prefix="/events",
)


events_router.get("/", response_model=list[GetEventList])
async def listevents(
    filter: Annotated[EventListFilterSchema, Depends(EventListFilterSchema)],
):
    return await get_event_service().get_event_list(filter)


@events_router.get("/sport_types", response_model=list[SportTypeSchema])
async def list_sport_types():
    return await get_sport_type_service().list_sport_types()


@events_router.get("/{event_id}", response_model=GetEvent)
async def get_event(event_id: UUID):
    return await get_event_service().get_event(event_id)


@events_router.post("/register", response_model=RegistrationSchema)
async def register_on_event(
    register: PostRegister, authorization: Annotated[str, Header()]
):
    return await get_registraton_service().regiser(register.ticket_id, authorization)


@events_router.get("/registrations/{ticket_id}", response_model=list[UserProfileSchema])
async def get_registered_esurs(ticket_id: UUID):
    return await get_registraton_service().get_registered_users(ticket_id)
