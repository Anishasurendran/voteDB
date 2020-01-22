from django.urls import path

from .views import LandingView, RegisterView
urlpatterns = [
    path("", LandingView.as_view(), name="dashboard"),
    path("register/", RegisterView.as_view(), name="join"),
]
