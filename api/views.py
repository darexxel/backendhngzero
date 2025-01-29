# api/views.py
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.http import require_GET

@require_GET
def get_info(request):
    return JsonResponse({
        "email": "daryjoe765@gmail.com",
        "current_datetime": timezone.now().isoformat(),
        "github_url": "https://github.com/darexxel/backendhngzero"
    })