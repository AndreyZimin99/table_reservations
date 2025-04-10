import datetime

from pydantic import BaseModel, ConfigDict, PositiveInt


class ReservationBase(BaseModel):
    customer_name: str
    table_id: int
    reservation_time: datetime.datetime
    duration_minutes: PositiveInt


class ReservationCreate(ReservationBase):
    pass


class Reservation(ReservationBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
