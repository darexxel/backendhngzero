from django.shortcuts import render


from django.http import JsonResponse
from django.utils import timezone

def get_info(request):
    data = {
        "email": "your-email@example.com",  # Replace with your HNG email
        "current_datetime": timezone.now().isoformat(),
        "github_url": "https://github.com/yourusername/hng_stage0"
    }
    return JsonResponse(data)