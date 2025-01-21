from fastapi import FastAPI
from api.seat_api import router as seat_roter
from api.book_api import router as book_router

app = FastAPI(title="Theater Reservation System")

@app.get("/")
def check_health():
    return {"message": "API is healthy!"}

# include other api
app.include_router(seat_roter)
app.include_router(book_router)