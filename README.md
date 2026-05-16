# Event Registration System

## Overview

Event Registration System is a backend API application developed using FastAPI and MongoDB Atlas. The project manages participants, events, registrations, waitlists, and event check-ins through REST APIs.

---

## Key Features

* Participant management
* Event creation and retrieval
* Event registration system
* Automatic waitlist handling
* Participant check-in functionality
* MongoDB Atlas database integration
* Swagger API documentation support

---

## Technology Stack

* Python
* FastAPI
* MongoDB Atlas
* Beanie ODM
* Pydantic
* Uvicorn

---

## Project Structure

```bash
Event_Registration_System/
│
├── app/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── database.py
│   └── main.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## API Endpoints

### Participant APIs

| Method | Endpoint                       |
| ------ | ------------------------------ |
| POST   | /participants                  |
| GET    | /participants/{participant_id} |

### Event APIs

| Method | Endpoint           |
| ------ | ------------------ |
| POST   | /events            |
| GET    | /events/{event_id} |

### Registration APIs

| Method | Endpoint                   |
| ------ | -------------------------- |
| POST   | /registrations             |
| PUT    | /checkin/{registration_id} |

---

## Installation

### Clone Repository

```bash
git clone https://github.com/kirthiga-2301/Event_Registration_System.git
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python -m uvicorn app.main:app --reload
```

---

## API Documentation

Swagger documentation:

```bash
http://127.0.0.1:8000/docs
