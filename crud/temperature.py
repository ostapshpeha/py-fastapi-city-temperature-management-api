from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.temperature import TemperatureCreate, Temperature


async def get_all_temperature_records(db: AsyncSession) -> list[Temperature]:
    result = await db.scalars(select(Temperature))

    return list(result.all())

async def get_temperature_for_city(db: AsyncSession, city_id: int) -> list[Temperature]:
    result = await db.scalars(
        select(Temperature).where(city_id=city_id)
    )
    return list(result.all())

async def update_temperature(db: AsyncSession, city_id: int, temperature: TemperatureCreate) -> Temperature:
    result = await db.scalars(
        select(Temperature).where(city_id=city_id)
    )
