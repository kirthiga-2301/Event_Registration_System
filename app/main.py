from fastapi import FastAPI
from app.database import init_db

from app.routes.participant_routes import router as participant_router
from app.routes.event_routes import router as event_router
from app.routes.registration_routes import router as registration_router

app = FastAPI()


@app.on_event("startup")
async def start_database():
    await init_db()


app.include_router(participant_router)
app.include_router(event_router)
app.include_router(registration_router)


@app.get("/")
async def root():
    return {
        "message": "Event Registration System API"
    }