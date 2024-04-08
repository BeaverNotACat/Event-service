from functools import lru_cache

from sqlalchemy import select

from src.database.models import SportType
from src.database.session import async_session_maker


class SportTypeServise:
    async def list_sport_types(self):
        session = async_session_maker()
        query = select(SportType)
        result = await session.execute(query)
        result = result.scalars().all()
        await session.close()
        return result


@lru_cache
def get_sport_type_service():
    return SportTypeServise()
