import json
from typing import List

from fastapi import APIRouter
from fastapi.params import Depends

from schema.theater_schema import Theater

router = APIRouter(prefix="/reservation")

# file path
file_path = "data.json"


def load_data() -> List[Theater]:
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data


@router.get("theaters/{theaterId}/seats")
def check_seats(theaterId: int, data: List[Theater] = Depends(load_data)):
    seat_count = 0
    for item in data:
        if item["theaterId"] == theaterId:
            seat_count = item["seats"]
    return seat_count
