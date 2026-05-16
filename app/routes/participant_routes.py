from fastapi import APIRouter
from app.models.participant_model import Participant
from app.services.participant_service import (
    create_participant_service,
    get_participant_service
)

router = APIRouter()


@router.post("/participants")
async def create_participant(participant: Participant):

    new_participant = await create_participant_service(participant)

    return {
        "success": True,
        "message": "Participant created successfully",
        "data": new_participant
    }


@router.get("/participants/{participant_id}")
async def get_participant(participant_id: str):

    participant = await get_participant_service(participant_id)

    return {
        "success": True,
        "data": participant
    }