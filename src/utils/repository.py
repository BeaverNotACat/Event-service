from abc import ABC, abstractmethod
from typing import BinaryIO
import uuid

from sqlalchemy import insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.base import ExecutableOption

from src.database.s3_storage import PublicAssetS3Storage


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data: dict) -> int:
        stmt = insert(self.model).values(**data).returning(self.model)  # type: ignore
        res = await self.session.execute(stmt)
        return res.scalar_one()

    async def edit_one(self, id: uuid.UUID, data: dict) -> int:
        stmt = (
            update(self.model)  # type: ignore
            .values(**data)
            .filter_by(id=id)
            .returning(self.model)  # type: ignore
        )
        res = await self.session.execute(stmt)
        return res.unique().scalar_one()

    async def find_all(self):
        stmt = select(self.model).options(*self.get_select_options())  # type: ignore
        res = await self.session.execute(stmt)
        return res.unique().scalars().fetchall()

    async def find_filtered(self, **filter_by):
        stmt = select(self.model).options(*self.get_select_options()).filter_by(**filter_by)  # type: ignore
        res = await self.session.execute(stmt)
        return res.unique().scalars().fetchall()

    async def find_one(self, **filter_by):
        stmt = (
            select(self.model)  # type: ignore
            .options(*self.get_select_options())
            .filter_by(**filter_by)
        )
        res = await self.session.execute(stmt)
        res = res.unique().scalar_one()
        return res

    async def delete_one(self, id: uuid.UUID):
        await self.session.delete((await self.find_one(id=id)))

    def get_select_options(self) -> list[ExecutableOption]:
        return []


class S3Repository(AbstractRepository):
    def __init__(self, session: PublicAssetS3Storage):
        self.session = session

    async def get_one(self, key: str):
        return await self.session.get_path(key)

    async def add_one(self, file: BinaryIO, key: str):
        return await self.session.write(file, key)

    async def delete_one(self, key):
        return await self.session.delete(key)
