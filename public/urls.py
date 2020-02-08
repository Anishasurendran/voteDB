from django.urls import path

from .views import LandingView, RegisterView, uploadXML, ConfirmView
urlpatterns = [
    path("", LandingView.as_view(), name="dashboard"),
    path("register/", RegisterView.as_view(), name="join"),
    path("confirm/<int:id>/profile/", ConfirmView.as_view(), name="confirm"),
    path("upload_xml/", uploadXML, name="xml_upload"),
]
