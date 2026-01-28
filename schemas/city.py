from typing import List

from pydantic import BaseModel
from schemas.temperature import Temperature


class CityBase(BaseModel):
    name: str
    additional_info: str

class CityCreate(CityBase):
    pass

class City(CityBase):
    id: int

    class Config:
        orm_mode = True

class CityFull(City):
    temperatures: List[Temperature] = []
