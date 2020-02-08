from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from authy.api import AuthyApiClient
from rest_framework.response import Response
from django.conf import settings

from zipfile import ZipFile
from datetime import datetime
import json
import xml.etree.ElementTree as ET

from .forms import UploadXMLForm, ProfileCompleteFrom, PhoneVerificationForm
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


def profile_complete(request):
    if request.method == "POST":
        profile_form = ProfileCompleteFrom(request.POST)
        if profile_form.is_valid():
            phone = profile_form.cleaned_data['phone']
            aadhar = profile_form.cleaned_data['aadhar']

            request.session['phone_number'] = phone

            authy_api.phones.verification_start(
                form.cleaned_data['phone_number'],
                '91',
                via='sms'
            )
            return Response({}, 200)
    else:
        form = VerificationForm()

def phone_verification(request):
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
                return redirect('verified')
            else:
                for error_msg in verification.errors().values():
                    form.add_error(None, error_msg)
        

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
