from beanie import Document
from pydantic import EmailStr
from typing import List


class Participant(Document):

    name: str
    age: int
    email: EmailStr
    city: str
    interests: List[str]