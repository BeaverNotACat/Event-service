import uuid

from fastapi import APIRouter, UploadFile
from sqlalchemy.sql.visitors import _TraverseTransformCallableType

from src.database.models import Article
from src.utils.dependencies import UnitOfWorkDep
from src.service.event import EventServise
from src.schemas.schemas import (
    CreateArticlePydantic,
    GetArticlePydantic,
    LanguageCode,
    GetEvent,
    GetEventList,
    CreateEvent,
    GetEventLocalisation,
    GetEventLocalisationList,
    CreateEventLocalisation,
)

v1_router = APIRouter(
    prefix="/api/v1/event-service",
)


@v1_router.get("/healthcheck")  # TODO Cmon Denis I want to remove this
async def healthcheck():
    return "success"


@v1_router.get("/events", response_model=GetEventList)  # TODO filters
async def list_events(unit_of_work: UnitOfWorkDep, limit: int = 100, page: int = 1):
    async with unit_of_work:
        return GetEventList.model_validate(
            await EventServise().get_event_list_paginated(unit_of_work, limit, page)
        )


@v1_router.post("/events", response_model=GetEvent)
async def create_event(unit_of_work: UnitOfWorkDep, data: CreateEvent):
    async with unit_of_work:
        return GetEvent.model_validate(
            await EventServise().create_event(unit_of_work, data.model_dump())
        )


@v1_router.get("/events/{id}", response_model=GetEvent)
async def get_event(unit_of_work: UnitOfWorkDep, id: uuid.UUID):
    async with unit_of_work:
        return GetEvent.model_validate(
            await EventServise().get_event_by_id(unit_of_work, id)
        )


@v1_router.get(
    "/events/{event_id}/localisations", response_model=GetEventLocalisationList
)
async def get_event_localisation(unit_of_work: UnitOfWorkDep, event_id: uuid.UUID):
    async with unit_of_work:
        return GetEventLocalisationList.model_validate(
            await EventServise().get_event_localisations(unit_of_work, event_id)
        )


@v1_router.post(
    "/events/{event_id}/localisations/{language_code}",
    response_model=GetEventLocalisation,
)
async def create_event_localisation(
    unit_of_work: UnitOfWorkDep,
    event_id: uuid.UUID,
    language_code: LanguageCode,
    localisation: CreateEventLocalisation,
):
    async with unit_of_work:
        return GetEventLocalisation.model_validate(
            await EventServise().create_event_localisation(
                unit_of_work,
                event_id,
                language_code.value,
                localisation.model_dump(),
            )
        )


@v1_router.post(
    "/events/{event_id}/localisations/{language_code}/banner",
    response_model=GetEventLocalisation,
)
async def create_event_localisation_banner(
    unit_of_work: UnitOfWorkDep,
    event_id: uuid.UUID,
    language_code: LanguageCode,
    banner: UploadFile,
):
    async with unit_of_work:
        return GetEventLocalisation.model_validate(
            await EventServise().create_event_localisation_banner(
                unit_of_work, event_id, language_code.value, banner
            )
        )


@v1_router.post(
    "/events/{event_id}/localisations/{language_code}/articles",
    response_model=GetArticlePydantic,
)
async def create_article(
    unit_of_work: UnitOfWorkDep,
    event_id: uuid.UUID,
    language_code: LanguageCode,
    article: CreateArticlePydantic,
):
    async with unit_of_work:
        return GetArticlePydantic.model_validate(
            await EventServise().create_article(
                unit_of_work, event_id, language_code, article.model_dump()
            )
        )
