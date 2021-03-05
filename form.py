from django import forms
from appdj.models import *
class contactform(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label='Email')
    subject = forms.CharField(required=False)

class gr(forms.ModelForm):

    class Meta:
        model = grounds
        fields = ('groundname', 'groundimage')



