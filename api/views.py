# api/views.py

from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])  # Optimize by only allowing GET requests
def get_info(request):
    # Get current UTC time in ISO 8601 format
    current_time = timezone.now().strftime('%Y-%m-%dT%H:%M:%SZ')
    
    data = {
        "email": "daryjoe765@gmail.com",
        "current_datetime": current_time,  # Dynamic UTC time
        "github_url": "https://github.com/darexxel/hng_stage0"  # Updated GitHub username
    }
    return JsonResponse(data, json_dumps_params={'separators': (',', ':')})  # Minimize JSON size