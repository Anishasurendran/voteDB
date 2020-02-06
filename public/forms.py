from django import forms


class UploadXMLForm(forms.Form):
    pass_code = forms.CharField(required=True)
    xml_file = forms.FileField(required=True)
