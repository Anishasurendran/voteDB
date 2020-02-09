from django import forms


class UploadXMLForm(forms.Form):
    pass_code = forms.CharField(required=True)
    xml_file = forms.FileField(required=True)

class ProfileCompleteFrom(forms.Form):
    aadhar = forms.CharField(required=True)
    phone =  forms.CharField(required= True)

class PhoneVerificationForm(forms.Form):
    verification_code = forms.CharField(required = True)

class PhotoUploadForm(forms.Form):
    profile_photo= forms.ImageField(required = True)