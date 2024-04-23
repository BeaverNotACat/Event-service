from src.database.unit_of_work import IUnitOfWork
from src.schemas.schemas import CreateSport


class SportServise:
    async def get_sports(self, unit_of_work: IUnitOfWork):
        return await unit_of_work.sport.find_all()

    async def create_sport(self, unit_of_work: IUnitOfWork, sport: CreateSport):
        res = await unit_of_work.sport.add_one_schema(sport)
        await unit_of_work.commit()
        return res
