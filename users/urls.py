from django.urls import path
from . import views

urlpatterns = [
    path('user/list/',views.UserDetailsList.as_view()),
    path('user/update/<int:pk>',views.UserDetailsUpdate.as_view()),
    path('verify/aadhar/', views.VerifyAadhar.as_view(), name="verify_aadhar"),
    path('verify/otp/<int:id>', views.PhoneVerification.as_view(), name="verify_phone"),
    path('verify/photo/<int:id>', views.PhotoVerification.as_view(), name="verify_phone")
]