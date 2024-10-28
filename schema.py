from pydantic import BaseModel
from typing import List


class Coordinate(BaseModel):
    latitude: float
    longitude: float


class CoordinateList(BaseModel):
    data: List[Coordinate]
