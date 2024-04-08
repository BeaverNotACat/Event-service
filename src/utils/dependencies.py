import typing

from fastapi import Depends

from src.database.unit_of_work import IUnitOfWork, UnitOfWork


UnitOfWorkDep = typing.Annotated[IUnitOfWork, Depends(UnitOfWork)]
