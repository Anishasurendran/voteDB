from django.urls import path
from . import views

urlpatterns = [
    path('user/list/',views.UserDetailsList.as_view()),
    path('user/update/<int:pk>',views.UserDetailsUpdate.as_view()),
     ]