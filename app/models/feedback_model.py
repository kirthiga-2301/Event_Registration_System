from beanie import Document
from pydantic import Field


class Feedback(Document):

    participant_id: str
    event_id: str
    rating: int = Field(ge=1, le=5)