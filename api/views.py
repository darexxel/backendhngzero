from django.shortcuts import render


from django.http import JsonResponse
from django.utils import timezone
from datetime import datetime

def get_info(request):
    # Get current UTC time
    current_time = timezone.now().strftime('%Y-%m-%dT%H:%M:%SZ')
    
    data = {
        "email": "daryjoe765@gmail.com",
        "current_datetime": current_time,  # Dynamic UTC time
        "github_url": "https://github.com/darad124/hng_stage0.git"  # Added .git
    }
    return JsonResponse(data)