from fastapi import APIRouter
from app.models.registration_model import Registration
from app.services.registration_service import (
    register_participant_service,
    check_in_service
)

router = APIRouter()


@router.post("/registrations")
async def register_participant(registration: Registration):

    new_registration = await register_participant_service(registration)

    return {
        "success": True,
        "message": "Registration completed",
        "data": new_registration
    }


@router.put("/checkin/{registration_id}")
async def check_in(registration_id: str):

    registration = await check_in_service(registration_id)

    return {
        "success": True,
        "message": "Participant checked in successfully",
        "data": registration
    }