from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/feedback",
    tags=["Feedback"]
)

feedback_list = []

class Feedback(BaseModel):
    participant_id: int
    event_id: int
    rating: int = Field(..., ge=1, le=5)
    comment: str

@router.post("/")
async def add_feedback(feedback: Feedback):

    feedback_data = feedback.dict()
    feedback_data["id"] = len(feedback_list) + 1

    feedback_list.append(feedback_data)

    return {
        "message": "Feedback added successfully",
        "data": feedback_data
    }


@router.get("/")
async def get_feedbacks():

    return {
        "message": "Feedback list fetched successfully",
        "data": feedback_list
    }


@router.get("/{feedback_id}")
async def get_feedback(feedback_id: int):

    for feedback in feedback_list:
        if feedback["id"] == feedback_id:
            return {
                "message": "Feedback found",
                "data": feedback
            }

    raise HTTPException(
        status_code=404,
        detail="Feedback not found"
    )


@router.delete("/{feedback_id}")
async def delete_feedback(feedback_id: int):

    for feedback in feedback_list:
        if feedback["id"] == feedback_id:

            feedback_list.remove(feedback)

            return {
                "message": "Feedback deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Feedback not found"
    )

