from pydantic import BaseModel


class Theater(BaseModel):
    theaterId: int
    seats: int
    name: str


