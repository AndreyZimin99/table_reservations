from pydantic import BaseModel, ConfigDict, PositiveInt


class TableBase(BaseModel):
    name: str
    seats: PositiveInt
    location: str


class TableCreate(TableBase):
    pass


class Table(TableBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
