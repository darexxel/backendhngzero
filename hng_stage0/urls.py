from django.urls import path
from api.views import get_info  # Import the view directly

urlpatterns = [
    path('', get_info, name='get_info'),  # Serve at root URL
]