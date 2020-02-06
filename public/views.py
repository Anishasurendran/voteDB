from django.shortcuts import render, redirect

from django.views.generic import TemplateView
from .forms import UploadXMLForm


class LandingView(TemplateView):
    template_name = 'landing.html'

class RegisterView(TemplateView):
    template_name= 'register.html'

def uploadXML(request):

    if request.method == "POST":
        UploadForm = UploadXMLForm(files=request.FILES)
        print(request.FILES)

        if UploadForm.is_valid():
            print(UploadForm.cleaned_data['xml_file'])
        else:
            print(UploadForm.errors)
    return redirect('/register/')