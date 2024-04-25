import uuid

from src.database.unit_of_work import IUnitOfWork
from src.schemas.schemas import CreateSport


class SportServise:
    async def get_sports(self, unit_of_work: IUnitOfWork):
        return await unit_of_work.sport.find_all()

    async def create_sport(self, unit_of_work: IUnitOfWork, sport: CreateSport):
        res = await unit_of_work.sport.add_one_schema(sport)
        await unit_of_work.commit()
        return res

    async def update_sport(
        self, unit_of_work: IUnitOfWork, id: uuid.UUID, data: CreateSport
    ):
        sport = await unit_of_work.sport.find_one(id=id)
        for language in sport.localizations:
            await unit_of_work.sport_localization.edit_one(
                id=sport.localizations[language].id,
                data=data.localizations[language].model_dump(),
            )
        await unit_of_work.commit()
        return await unit_of_work.sport.find_one(id=id)

    async def delete_sport(self, unit_of_work: IUnitOfWork, id: uuid.UUID) -> None:
        await unit_of_work.sport.delete_one(id=id)
        await unit_of_work.commit()
