import functools

from fastapi import HTTPException
from sqlalchemy.exc import NoResultFound


def no_result_404(func):  # TODO rename
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except NoResultFound:
            raise HTTPException(404, "No resource was found")

    return wrapper


def validate_organiser_rights(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        # TODO tocken validation
        return await func(*args, **kwargs)

    return wrapper
