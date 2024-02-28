"""
Jordyn Kuhn
CIS 218
2-28-2024
"""
from django.urls import path
from .views import SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup")
]