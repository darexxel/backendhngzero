from django.shortcuts import render


from django.http import JsonResponse
from django.utils import timezone

def get_info(request):
    data = {
        "email": "daryjoe765@gmail.com",
        "current_datetime": timezone.now().isoformat(),
        "github_url": "https://github.com/darad124/hng_stage0"
    }
    return JsonResponse(data)