from beanie import Document
from typing import Optional


class Registration(Document):

    participant_id: str
    event_id: str
    status: str
    checked_in: bool = False