import typing
import uuid

from fastapi import HTTPException, UploadFile

from src.database.s3_storage import s3_session_maker
from src.database.unit_of_work import IUnitOfWork
from src.database.models import Event, EventLocalisation
from src.utils.validations import no_result_404, check_tocken


class EventServise:
    async def get_event_list_paginated(
        self,
        unit_of_work: IUnitOfWork,
        limit: int,
        page: int,
    ) -> list[Event]:
        if page <= 0 or limit <= 0:
            HTTPException(400, "Page and limit must be positive not null")
        offset = limit * (page - 1)
        return await unit_of_work.event.find_all_paginated(limit, offset)  # type: ignore

    @no_result_404
    async def get_event_by_id(self, unit_of_work: IUnitOfWork, id: uuid.UUID) -> Event:
        return await unit_of_work.event.find_one(id=id)

    @no_result_404
    async def get_event_localisations(
        self, unit_of_work: IUnitOfWork, event_id: uuid.UUID
    ) -> list[EventLocalisation]:
        await unit_of_work.event.find_one(id=event_id)
        return await unit_of_work.event_localisation.find_filtered(
            event_id=event_id
        )  # type: ignore

    @check_tocken
    async def create_event(
        self, unit_of_work: IUnitOfWork, data: dict[str, typing.Any]
    ) -> Event:
        id = await unit_of_work.event.add_one(data)
        await unit_of_work.commit()
        return await unit_of_work.event.find_one(id=id)

    @check_tocken
    @no_result_404
    async def create_event_localisation(
        self,
        unit_of_work: IUnitOfWork,
        event_id: uuid.UUID,
        language_code: str,
        localisation_data: dict[str, typing.Any],
    ) -> EventLocalisation:
        await unit_of_work.event.find_one(id=event_id)  # Checks is event exists

        localisation_data["event_id"] = event_id
        localisation_data["language_code"] = language_code
        localisation_id = await unit_of_work.event_localisation.add_one(
            localisation_data
        )
        await unit_of_work.commit()
        return await unit_of_work.event_localisation.find_one(id=localisation_id)

    @check_tocken
    @no_result_404
    async def create_event_localisation_banner(
        self,
        unit_of_work: IUnitOfWork,
        event_id: uuid.UUID,
        language_code: str,
        banner: UploadFile,
    ) -> EventLocalisation:
        localisation = await unit_of_work.event_localisation.find_one(
            event_id=event_id, language_code=language_code
        )

        localisation_id = await unit_of_work.event_localisation.edit_one(
            id=localisation.id,
            data={
                "banner_filename": s3_session_maker().write(
                    banner.file, banner.filename
                )
            },
        )
        await unit_of_work.commit()
        return await unit_of_work.event_localisation.find_one(id=localisation_id)

    @check_tocken
    async def create_article(
        self,
        unit_of_work: IUnitOfWork,
        event_id: uuid.UUID,
        language_code: str,
        data: dict[str, typing.Any],
    ) -> Event:
        localisation = await unit_of_work.event_localisation.find_one(
            event_id=event_id, language_code=language_code
        )
        data["event_translation_id"] = localisation.id
        article_id = await unit_of_work.article.add_one(data)
        await unit_of_work.commit()
        return await unit_of_work.article.find_one(id=article_id)

    def update_event(self): ...

    def delete_event(self): ...
