# api/views.py

from django.http import JsonResponse
from django.utils import timezone

def get_info(request):
    # Get current UTC time in ISO 8601 format
    current_time = timezone.now().strftime('%Y-%m-%dT%H:%M:%SZ')
    
    data = {
        "email": "daryjoe765@gmail.com",
        "current_datetime": current_time,  # Dynamic UTC time
        "github_url": "https://github.com/darad124/hng_stage0"  # Removed .git
    }
    return JsonResponse(data)