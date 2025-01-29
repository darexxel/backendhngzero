# api/views.py

from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def get_info(request):
    current_time = timezone.now().strftime('%Y-%m-%dT%H:%M:%SZ')
    data = {
        "email": "daryjoe765@gmail.com",
        "current_datetime": current_time,
        "github_url": "https://github.com/darexxel/backendhngzero"
    }
    response = JsonResponse(data, json_dumps_params={'separators': (',', ':')})
    response["Access-Control-Allow-Origin"] = "*"  # Explicit header
    return response