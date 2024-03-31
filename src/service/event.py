from uuid import UUID
from datetime import datetime
from functools import lru_cache

from sqlalchemy import select
from fastapi import HTTPException
from sqlalchemy.orm import selectinload

from src.schemas.event import EventListFilterSchema
from src.database.models import Event, Place, Ticket
from src.database.session import async_session_maker


class EventServise:
    async def get_event_list(self, filter: EventListFilterSchema, page=None, size=None):
        session = async_session_maker()
        query = (
            select(Event)
            .join(Place)
            .options(
                selectinload(Event.place).selectinload(Place.country),
                selectinload(Event.tickets).selectinload(Ticket.sport_type),
                selectinload(Event.target_group),
                selectinload(Event.sport_type),
            )
        )

        if filter.sport_type:
            query = query.filter(Event.sport_type_id == filter.sport_type).join(
                Event.sport_type
            )
        if filter.start_date:
            query = query.filter(Event.participation_start >= filter.start_date)
        if filter.end_date:
            query = query.filter(Event.participation_end <= filter.end_date)
        if filter.is_avaliable:
            query = query.filter(Event.registration_start <= datetime.utcnow())
            query = query.filter(Event.registration_end >= datetime.utcnow())
        if filter.search:
            query = query.filter(Event.title.ilike(f"%{filter.search}%"))

        result = await session.execute(query)
        await session.close()
        return result.scalars().all()

    async def get_event(self, event_id: UUID):
        session = async_session_maker()
        query = (
            select(Event)
            .filter(Event.id == event_id)
            .options(
                selectinload(Event.place).selectinload(Place.country),
                selectinload(Event.target_group),
                selectinload(Event.documents),
                selectinload(Event.starter_items),
                selectinload(Event.articles),
                selectinload(Event.tickets).selectinload(Ticket.sport_type),
                selectinload(Event.sport_type),
                selectinload(Event.social_links),
            )
        )
        result = await session.execute(query)
        result = result.scalar_one_or_none()
        await session.close()
        if not result:
            raise HTTPException(status_code=400, detail="Event not found")
        return result

    def create_event(self): ...

    def update_event(self): ...

    def delete_event(self): ...


@lru_cache
def get_event_service():
    return EventServise()
