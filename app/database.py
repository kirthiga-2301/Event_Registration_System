from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

DATABASE_NAME = "event_registration_db"

from app.models.participant_model import Participant
from app.models.event_model import Event
from app.models.registration_model import Registration
from app.models.feedback_model import Feedback


async def init_db():

    client = AsyncIOMotorClient(MONGO_URL)

    db = client[DATABASE_NAME]

    await init_beanie(
        database=db,
        document_models=[
            Participant,
            Event,
            Registration,
            Feedback
        ]
    )