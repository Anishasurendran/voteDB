from django.contrib import admin

# Register your models here.
from .models import CandidateDetails,Election, Location, Electioninfo, Voting

from rangefilter.filter import DateRangeFilter

@admin.register(CandidateDetails)
class CandidateDetailsAdmin(admin.ModelAdmin):
    list_display=('candidate_name','cand_district','cand_phoneno',)
    ordering=('candidate_name','cand_phoneno',)
    search_fields=('candidate_name',)

@admin.register(Election)
class ElectionAdmin(admin.ModelAdmin):
    list_display=('election_name','election_sdate','election_edate',)
    ordering=('election_name','election_sdate','election_edate',)
    search_fields=('election_name',)
    list_filter = ( ('election_sdate', DateRangeFilter),('election_edate', DateRangeFilter),)
    
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display=('location',)

@admin.register(Electioninfo)
class ElectionAdmin(admin.ModelAdmin):
    list_display=('election','candidate',)
    ordering=('election','candidate',)
    search_fields=('election',)
    list_filter = ('election',)

@admin.register(Voting)
class VotingAdmin(admin.ModelAdmin):
    list_display=('election','vote',)
    ordering=('election__id','vote',)
    search_fields=('vote',)
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
