import json
from typing import List

from fastapi import APIRouter, Depends

from schema.theater_schema import Theater

router = APIRouter(prefix="/reservation")

# file path
file_path = "data.json"

def load_data() -> List[Theater]:
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data



@router.post("/theaters/{theaterId}/book")
def book_seat(theaterId: int, data: List[Theater] = Depends(load_data)):

    for item in data:
        if item["theaterId"] == theaterId:
            count = item["seats"] -1

    return {"message": f" One seat reserved for {theaterId} and remaining seats are {count}"}