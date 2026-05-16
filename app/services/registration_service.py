from app.models.registration_model import Registration
from app.models.participant_model import Participant
from app.models.event_model import Event
from fastapi import HTTPException


async def register_participant_service(registration_data):

    participant = await Participant.get(registration_data.participant_id)

    if not participant:
        raise HTTPException(
            status_code=404,
            detail="Participant not found"
        )

    event = await Event.get(registration_data.event_id)

    if not event:
        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )

    existing_registration = await Registration.find_one(
        Registration.participant_id == registration_data.participant_id,
        Registration.event_id == registration_data.event_id
    )

    if existing_registration:
        raise HTTPException(
            status_code=400,
            detail="Participant already registered for this event"
        )

    registration_status = "confirmed"

    if event.available_seats <= 0:
        registration_status = "waitlisted"
    else:
        event.available_seats -= 1
        await event.save()

    registration = Registration(
        participant_id=registration_data.participant_id,
        event_id=registration_data.event_id,
        status=registration_status,
        checked_in=False
    )

    await registration.insert()

    return registration


async def check_in_service(registration_id: str):

    registration = await Registration.get(registration_id)

    if not registration:
        raise HTTPException(
            status_code=404,
            detail="Registration not found"
        )

    registration.checked_in = True

    await registration.save()

    return registration