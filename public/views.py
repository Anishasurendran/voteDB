from django.shortcuts import render, redirect

from django.views.generic import TemplateView
from .forms import UploadXMLForm

from zipfile import ZipFile
import xml.etree.ElementTree as ET


class LandingView(TemplateView):
    template_name = 'landing.html'


class RegisterView(TemplateView):
    template_name = 'register.html'


def uploadXML(request):

    if request.method == "POST":
        UploadForm = UploadXMLForm(request.POST, request.FILES)

        if UploadForm.is_valid():
            print(UploadForm.cleaned_data['pass_code'])
            extracted = ''
            userData = {}
            with ZipFile(UploadForm.cleaned_data['xml_file']) as zf:
                length = len(zf.filename) - 4
                extracted = zf.extract(
                    zf.filename[:length]+'.xml', path="./files", pwd=b'5aef')
            tree = ET.parse(extracted)
            root = tree.getroot()
            for element in root.find('UidData'):
                if not element.tag == 'Pht':
                    userData.update(element.attrib)
            print(userData)
        else:
            print(UploadForm.errors)
    return redirect('/register/')
