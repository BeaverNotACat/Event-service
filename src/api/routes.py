import uuid

from fastapi import APIRouter, HTTPException, UploadFile

from src.service.sport import SportServise
from src.utils.dependencies import UnitOfWorkDep
from src.service.event import EventServise
from src.schemas.schemas import (
    CreateDocument,
    CreateSport,
    GetSport,
    GetSportList,
    LanguageCode,
    GetEvent,
    GetEventList,
    CreateEvent,
)

v1_router = APIRouter(
    prefix="/api/v1/event-service",
)


@v1_router.get("/sports", tags=["sport"], response_model=GetSportList)  # TODO filters
async def list_sport_types(unit_of_work: UnitOfWorkDep):
    async with unit_of_work:
        return GetSportList.model_validate(
            await SportServise().get_sports(unit_of_work)
        )


@v1_router.post("/sports", tags=["sport"], response_model=GetSport)  # TODO filters
async def create_sport_types(unit_of_work: UnitOfWorkDep, sport: CreateSport):
    async with unit_of_work:
        return GetSport.model_validate(
            await SportServise().create_sport(unit_of_work, sport)
        )


@v1_router.get("/events", tags=["events"], response_model=GetEventList)  # TODO filters
async def list_events(unit_of_work: UnitOfWorkDep, limit: int = 100, page: int = 1):
    async with unit_of_work:
        return GetEventList.model_validate(
            await EventServise().get_event_list_paginated(unit_of_work, limit, page)
        )


@v1_router.post("/events", tags=["events"], response_model=GetEvent)
async def create_event(unit_of_work: UnitOfWorkDep, data: CreateEvent):
    async with unit_of_work:
        return GetEvent.model_validate(
            await EventServise().create_event(unit_of_work, data)
        )


@v1_router.get("/events/{id}", tags=["events"], response_model=GetEvent)
async def get_event(unit_of_work: UnitOfWorkDep, id: uuid.UUID):
    async with unit_of_work:
        return GetEvent.model_validate(await EventServise().get_event(unit_of_work, id))


@v1_router.put(
    "/events/{event_id}/localisations/{language_code}/banner",
    tags=["events"],
    response_model=GetEvent,
)
async def create_event_localisation_banner(
    unit_of_work: UnitOfWorkDep,
    event_id: uuid.UUID,
    language_code: LanguageCode,
    banner: UploadFile,
):
    async with unit_of_work:
        if not banner.filename:
            HTTPException(status_code=400, detail="Banner filename is missing")

        return GetEvent.model_validate(
            await EventServise().update_event_banner(
                unit_of_work, event_id, language_code.value, banner
            )
        )


@v1_router.post(
    "/events/{event_id}/documents",
    tags=["events"],
    response_model=GetEvent,
)
async def create_document(
    unit_of_work: UnitOfWorkDep, event_id: uuid.UUID, document: CreateDocument
):
    async with unit_of_work:
        return GetEvent.model_validate(
            await EventServise().create_event_document(
                unit_of_work, event_id, document.title
            )
        )


@v1_router.patch(
    "/events/{event_id}/documents/{title}",
    tags=["events"],
    response_model=GetEvent,
)
async def upload_document(
    unit_of_work: UnitOfWorkDep, event_id: uuid.UUID, title: str, document: UploadFile
):
    async with unit_of_work:
        if not document.filename:
            HTTPException(status_code=400, detail="Dpcument filename is missing")

        return GetEvent.model_validate(
            await EventServise().upload_document(
                unit_of_work, event_id, title, document
            )
        )
