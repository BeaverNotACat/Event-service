from functools import lru_cache
from fastapi import HTTPException
from sqlalchemy import select, insert, func

from src.database.models import Ticket, TicketRegistration
from src.database.session import async_session_maker
from src.schemas.registration import RegistrationSchema
from src.service.auth import get_auth_service


class RegistrationService:
    async def get_registered_users(self, ticket_id):
        request = select(TicketRegistration.user_id).filter(
            TicketRegistration.ticket_id == ticket_id
        )
        async with async_session_maker() as session:
            result = await session.execute(request)
        return await get_auth_service().get_users_list(result.scalars().all())

    async def count_registered_users(self, ticket_id):
        request = select(func.count(TicketRegistration.id)).filter(
            TicketRegistration.ticket_id == ticket_id
        )
        async with async_session_maker() as session:
            result = await session.execute(request)
        return result.scalar()

    async def is_user_registered(self, ticket_id, token):
        request = select(TicketRegistration).filter(
            TicketRegistration.ticket_id == ticket_id,
            TicketRegistration.user_id
            == (await get_auth_service().authenticate(token)).id,
        )
        async with async_session_maker() as session:
            result = await session.execute(request)
            return bool(result.scalar_one_or_none())

    async def regiser(self, ticket_id, token):
        request = select(Ticket.max_places).filter(Ticket.id == ticket_id)
        async with async_session_maker() as session:
            result = await session.execute(request)
            max_places = result.scalar()

        serial_number = await self.count_registered_users(ticket_id) + 1
        if max_places < serial_number:
            raise HTTPException(status_code=403, detail="All places are taken")
        if await self.is_user_registered(ticket_id, token):
            raise HTTPException(status_code=403, detail="You have already registered")

        request = insert(TicketRegistration).values(
            ticket_id=ticket_id,
            user_id=(user_id := (await get_auth_service().authenticate(token)).id),
            serial_number=serial_number,
        )
        async with async_session_maker() as session:
            await session.execute(request)
            await session.commit()
        return RegistrationSchema(ticket_id=ticket_id, user_id=user_id)


@lru_cache
def get_registraton_service():
    return RegistrationService()
