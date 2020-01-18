from django.contrib import admin

# Register your models here.
from .models import CandidateDetails,Election,Voting,Electioninfo

@admin.register(CandidateDetails)
class CandidateDetailsAdmin(admin.ModelAdmin):
    list_display=('candidate_name','candidate_district','candidate_phoneno',)
    ordering=('candidate_name','candidate_phoneno',)
    search_fields=('candidate_name',)
@admin.register(Election)
class Election(admin.ModelAdmin):
    list_display=('election_name','election_sdate','election_edate',)
    ordering=('election_name','election_sdate','election_eadte',)
    search_fields=('election_name')