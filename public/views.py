from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from authy.api import AuthyApiClient
from rest_framework.response import Response
from django.conf import settings
from django.http import HttpResponse
import base64
from PIL import Image
from io import BytesIO




from zipfile import ZipFile
from datetime import datetime
import json
import xml.etree.ElementTree as ET

from .forms import UploadXMLForm, ProfileCompleteFrom, PhoneVerificationForm, PhotoUploadForm
from .models import TempData
from .serializers import TempDataSerializers



authy_api = AuthyApiClient(settings.ACCOUNT_SECURITY_API_KEY)


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

class PhotoUploadView(TemplateView):
    template_name = 'photo_page.html'

    def get(self, request, id,  **kwargs):
        context = {}
        queryset = TempData.objects.get(pk=id)
        serializer = TempDataSerializers(queryset, many=False)
        context['profile'] = serializer.data
        return self.render_to_response(context)


def profile_complete(request, id):
    if request.method == "POST":
        profile_form = ProfileCompleteFrom(request.POST)
        if profile_form.is_valid():
            phone = profile_form.cleaned_data['phone']
            aadhar = profile_form.cleaned_data['aadhar']

            request.session['phone_number'] = phone

            authy_api.phones.verification_start(
                profile_form.cleaned_data['phone'],
                '91',
                via='sms'
            )
            return HttpResponse("Done")
    else:
        form = VerificationForm()

def phone_verification(request, id):
    if request.method == "POST":
        verification_form = PhoneVerificationForm(request.POST)
        if verification_form.is_valid():
            verification_code = verification_form.cleaned_data['verification_code']
            verification = authy_api.phones.verification_check(
                request.session['phone_number'],
                '91',
                verification_code
            )
            if verification.ok():
                request.session['is_verified'] = True
                return redirect('/confirm/'+str(id)+'/photo')
            else:
                for error_msg in verification.errors().values():
                    verification_form.add_error(None, error_msg)
        

def image_upload(request, id):
    if request.method == "POST":
        upload_form = PhotoUploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            im = Image.open(BytesIO(base64.b64decode(upload_form.cleaned_data['profile_photo'])))
            im.save('image.png', 'PNG')
            print(im)
            return HttpResponse("Done")
        else:
            print(upload_form.errors)
            return HttpResponse("Error")
            
    else:
        form =  PhotoUploadForm()
        

def uploadXML(request):

    if request.method == "POST":
        UploadForm = UploadXMLForm(request.POST, request.FILES)

        if UploadForm.is_valid():
            extracted = ''
            userData = {}
            with ZipFile(UploadForm.cleaned_data['xml_file']) as zf:
                length = len(zf.filename) - 4
                extracted = zf.extract(
                    zf.filename[:length]+'.xml', path="./files", pwd=b'1234')
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
