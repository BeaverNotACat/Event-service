from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from src.settings import get_settings


engine = create_async_engine(get_settings().postgres_url)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)
