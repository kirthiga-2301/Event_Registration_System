from app.models.participant_model import Participant
from fastapi import HTTPException


async def create_participant_service(participant_data):

    participant = Participant(**participant_data.dict())

    await participant.insert()

    return participant


async def get_participant_service(participant_id: str):

    participant = await Participant.get(participant_id)

    if not participant:
        raise HTTPException(
            status_code=404,
            detail="Participant not found"
        )

    return participant