from beanie import Document
from typing import List
from datetime import date


class Event(Document):

    title: str
    speaker_name: str
    date: date
    location: str
    topics: List[str]
    seat_limit: int
    available_seats: int