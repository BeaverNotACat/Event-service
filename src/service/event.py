import uuid

from fastapi import UploadFile

from src.database.unit_of_work import IUnitOfWork
from src.utils.validations import validate_organiser_rights
from src.schemas.schemas import CreateEvent


class EventServise:
    async def get_event_list_paginated(
        self, unit_of_work: IUnitOfWork, limit: int, page: int
    ):
        offset = limit * (page - 1)
        return await unit_of_work.event.find_all_paginated(limit, offset)

    async def get_event(self, unit_of_work: IUnitOfWork, id: uuid.UUID):
        return await unit_of_work.event.find_one(id=id)

    @validate_organiser_rights
    async def create_event(self, unit_of_work: IUnitOfWork, event: CreateEvent):
        res = await unit_of_work.event.add_one_schema(event)
        await unit_of_work.commit()
        return res

    @validate_organiser_rights
    async def update_event_banner(
        self,
        unit_of_work: IUnitOfWork,
        event_id: uuid.UUID,
        language_code: str,
        file: UploadFile,
    ):
        key = await unit_of_work.s3.add_one(file.file, file.filename)
        event = await unit_of_work.event.find_one(id=event_id)
        if event.localizations[language_code].banner_filename != "default.png":
            await unit_of_work.s3.delete_one(
                event.localizations[language_code].banner_filename
            )

        await unit_of_work.event_localization.edit_one(
            id=event.localizations[language_code].id, data={"banner_filename": key}
        )

        await unit_of_work.commit()
        return await unit_of_work.event.find_one(id=event_id)

    @validate_organiser_rights
    async def create_event_document(
        self, unit_of_work: IUnitOfWork, event_id: uuid.UUID, title: str
    ):
        await unit_of_work.document.add_one(
            {
                "event_id": event_id,
                "title": title,
                "filename": "default.pdf",
            }
        )
        await unit_of_work.commit()
        return await unit_of_work.event.find_one(id=event_id)

    @validate_organiser_rights
    async def upload_document(
        self,
        unit_of_work: IUnitOfWork,
        event_id: uuid.UUID,
        title: str,
        file: UploadFile,
    ):
        key = await unit_of_work.s3.add_one(file.file, file.filename)
        document = await unit_of_work.document.find_one(event_id=event_id, title=title)
        document.filename = key
        await unit_of_work.document.edit_one(id=document.id, data={"filename": key})
        await unit_of_work.commit()
        return await unit_of_work.event.find_one(id=event_id)
