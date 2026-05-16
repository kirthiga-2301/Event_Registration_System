from app.models.event_model import Event
from fastapi import HTTPException


async def create_event_service(event_data):

    event = Event(**event_data.dict())

    await event.insert()

    return event


async def get_event_service(event_id: str):

    event = await Event.get(event_id)

    if not event:
        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )

    return event