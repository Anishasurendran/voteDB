from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import UploadXMLForm
from .models import TempData
from .serializers import TempDataSerializers

from zipfile import ZipFile
from datetime import datetime
import json
import xml.etree.ElementTree as ET


class LandingView(TemplateView):
    template_name = 'landing.html'


class RegisterView(TemplateView):
    template_name = 'register.html'


class ConfirmView(TemplateView):
    template_name = 'confirm_page.html'

    def get(self, request, id,  **kwargs):
        context = {}
        queryset = TempData.objects.get(pk=id)
        serializer = TempDataSerializers(queryset, many=False)
        context['profile'] = serializer.data
        return self.render_to_response(context)


def uploadXML(request):

    if request.method == "POST":
        UploadForm = UploadXMLForm(request.POST, request.FILES)

        if UploadForm.is_valid():
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
            dob = datetime.strptime(userData['dob'], '%d-%m-%Y')
            print(dob)

            tempData = TempData.objects.create(
                dob=dob,
                gender=userData['gender'],
                name=userData['name'],
                careof=userData['careof'],
                dist=userData['dist'],
                address=userData['house'] + ', ' + userData['street'] +
                ', ' + userData['vtc'] + ', ' + userData['state'],
                pin=userData['pc']
            )
            print(tempData)

        else:
            print(UploadForm.errors)
    return redirect('/confirm/'+str(tempData.id)+'/profile')
