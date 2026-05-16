from fastapi import APIRouter
from app.models.event_model import Event
from app.services.event_service import (
    create_event_service,
    get_event_service
)

router = APIRouter()


@router.post("/events")
async def create_event(event: Event):

    new_event = await create_event_service(event)

    return {
        "success": True,
        "message": "Event created successfully",
        "data": new_event
    }


@router.get("/events/{event_id}")
async def get_event(event_id: str):

    event = await get_event_service(event_id)

    return {
        "success": True,
        "data": event
    }