from pydantic import BaseModel
from typing import Optional

class CarResponse(BaseModel):
    number: Optional[int]
    car_id: str
    zone: Optional[str]
    zone_number: Optional[str]

    class Config:
        orm_mode = True
