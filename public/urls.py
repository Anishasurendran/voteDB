from django.urls import path

from .views import LandingView, RegisterView, uploadXML
urlpatterns = [
    path("", LandingView.as_view(), name="dashboard"),
    path("register/", RegisterView.as_view(), name="join"),
    path("upload_xml/", uploadXML, name="xml_upload"),
]
