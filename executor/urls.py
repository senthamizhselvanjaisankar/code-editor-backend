from django.urls import path
from .views import execute_code

urlpatterns = [
    path('execute/', execute_code),
]
