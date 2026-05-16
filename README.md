# Event Registration System

## Project Overview
This project is built using FastAPI and MongoDB Atlas.

It allows:
- Creating participants
- Creating events
- Registering participants for events
- Waitlist handling when seats are full
- Participant check-in

## Technologies Used
- FastAPI
- MongoDB Atlas
- Beanie ODM
- Python

## Setup Steps

### Create Virtual Environment
python -m venv venv

### Activate Virtual Environment
venv\Scripts\activate

### Install Requirements
pip install -r requirements.txt

### Run Server
python -m uvicorn app.main:app --reload

## Swagger URL
http://127.0.0.1:8000/docs

## APIs

### Participants
POST /participants
GET /participants/{participant_id}

### Events
POST /events
GET /events/{event_id}

### Registrations
POST /registrations

### Check-in
PUT /checkin/{registration_id}