from fastapi import FastAPI
from app.core.database import ping_db
from app.api.routers import habits_routes

app = FastAPI(title="Habit Tracker API")


@app.on_event("startup")
def startup():
    ping_db()


app.include_router(habits_routes.router)