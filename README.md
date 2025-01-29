# HNG Stage 0 Backend Task

A Django API that returns user info, current UTC time, and GitHub repo URL.

## Setup

1. Clone the repo: `git clone https://github.com/darad124/hng_stage0.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `python manage.py runserver`

## API Endpoint

- **URL:** `GET /`
- **Response:**

  ```json
  {
    "email": "daryjoe765@gmail.com",
    "current_datetime": "2023-09-20T12:34:56.789Z",
    "github_url": "https://github.com/darad124/hng_stage0"
  }
  