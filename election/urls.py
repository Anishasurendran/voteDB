from django.urls import path
from . import views

urlpatterns = [
    path('candidate/list/',views.CandidateDetailsList.as_view()),
    path('candidate/update/<int:pk>/',views.CandidateDetailsUpdate.as_view()),
    path('election/list/',views.ElectionList.as_view()),
    path('election/<int:pk>/',views.ElectionCandidateList.as_view()),
    path('voting/<int:id>',views.VoteView.as_view()),
]