# HNG Stage 0 Backend Task

A Django API that returns user info, current UTC time, and GitHub repo URL.

## API Endpoints

- **Production URL:** `https://backendhngzero.onrender.com`
- **Local URL:** `http://localhost:8000/`

## Response Example

```json
{
    "email": "daryjoe765@gmail.com",
    "current_datetime": "2025-01-29T18:25:11Z",
    "github_url": "https://github.com/darexxel/hng_stage0"
}
```

## Local Setup

1. Clone the repo: `git clone https://github.com/darad124/hng_stage0.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `python manage.py runserver`
  