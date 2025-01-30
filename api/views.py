# api/views.py
from django.http import JsonResponse
from datetime import datetime, timezone
from django.views.decorators.http import require_GET

@require_GET
def get_info(request):
    # Format: YYYY-MM-DDTHH:MM:SSZ (no milliseconds, no timezone offset)
    current_time = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    
    data = {
        "email": "daryjoe765@gmail.com",
        "current_datetime": current_time,
        "github_url": "https://github.com/darexxel/backendhngzero"
    }
    return JsonResponse(data)