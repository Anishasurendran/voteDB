from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import LandingView, RegisterView,RegistrationCompleteView, uploadXML, ConfirmView, PhotoUploadView, phone_verification, profile_complete, image_upload


urlpatterns = [
    path("", LandingView.as_view(), name="dashboard"),
    path("register/", RegisterView.as_view(), name="join"),
    path("confirm/<int:id>/profile/", ConfirmView.as_view(), name="confirm"),
    path("confirm/<int:id>/photo/", PhotoUploadView.as_view(), name="confirm"),
    path("confirm/complete/", RegistrationCompleteView.as_view(), name="completed_profile"),
    path("upload_xml/", uploadXML, name="xml_upload"),
    path("profile_complete/<int:id>/", profile_complete, name="profile_complete"),
    path("phone_verification/<int:id>/", phone_verification, name="phone_verification"),
    path("image_upload/<int:id>/", image_upload, name="image_upload")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
