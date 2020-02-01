from django.urls import path
from . import views

urlpatterns = [
    path('candidate/list/',views.CandidateDetailsList.as_view()),
    path('candidate/update/',views.CandidateDetailsUpdate.as_view()),
    path('election/list/',views.ElectionList.as_view()),
    path('voting/create/',views.VotingCreate.as_view()),
    path('voting/update/',views.VotingUpdate.as_view()),
     ]