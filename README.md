# HNG Stage 0 Backend Task (Python/Django)

A production-ready API endpoint that returns:

- Registered email address
- Current UTC datetime in ISO 8601 format
- GitHub repository URL

**Live API Endpoint:** `https://backendhngzero.vercel.app/api/`

## :rocket: API Documentation

```http
GET /api/
Host: backendhngzero.vercel.app
```

### Successful Response (200 OK)

```json
{
    "email": "daryjoe765@gmail.com",
    "current_datetime": "2024-05-15T14:30:00Z",  // Dynamically generated UTC time
    "github_url": "https://github.com/darexxel/backendhngzero"
}
```

## :computer: Local Development Setup

1. **Clone Repository**

   ```bash
   git clone https://github.com/darexxel/hng-backend-stage-zero.git
   cd hng-backend-stage-zero
   ```

2. **Create Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run Development Server**

   ```bash
   python manage.py runserver
   ```

   Access locally: `http://localhost:8000/api/`

## :globe_with_meridians: Deployment

Hosted on Vercel with Django configuration. The API:

- Automatically deploys from GitHub main branch
- Handles CORS for cross-origin requests
- Provides SSL encryption

## :hourglass_flowing_sand: Response Validation

The `current_datetime` field updates every second:

```bash
# Test dynamic time (Unix)
curl https://backendhngzero.vercel.app/api/ | grep current_datetime
```

---

[Hire Python Developers via HNG](https://hng.tech/hire/python-developers)
