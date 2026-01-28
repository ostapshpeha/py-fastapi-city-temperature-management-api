from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.city import CityCreate, City


async def get_all_cities(db: AsyncSession) -> list[City]:
    result = await db.scalars(select(City))

    return list(result.all())


async def create_city(db: AsyncSession, city_data: CityCreate) -> City:
    db_city = City(**city_data.model_dump())
    db.add(db_city)
    await db.commit()
    await db.refresh(db_city)

    return db_city

async def delete_city(db: AsyncSession, city_id: int) -> None:
    db_city = await db.scalars(select(City).where(id == city_id))
    await db.delete(db_city)
