from django.urls import path

from .views import LandingView, RegisterView, uploadXML, ConfirmView, PhotoUploadView, phone_verification, profile_complete, image_upload
urlpatterns = [
    path("", LandingView.as_view(), name="dashboard"),
    path("register/", RegisterView.as_view(), name="join"),
    path("confirm/<int:id>/profile/", ConfirmView.as_view(), name="confirm"),
    path("confirm/<int:id>/photo/", PhotoUploadView.as_view(), name="confirm"),
    path("upload_xml/", uploadXML, name="xml_upload"),
    path("profile_complete/<int:id>/", profile_complete, name="profile_complete"),
    path("phone_verification/<int:id>/", phone_verification, name="phone_verification"),
    path("image_upload/<int:id>/", image_upload, name="image_upload")
]
