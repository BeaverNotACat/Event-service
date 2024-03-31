import asyncio

from src.database.session import engine

from src.database.models import Base


async def migrate_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    asyncio.run(migrate_models())
