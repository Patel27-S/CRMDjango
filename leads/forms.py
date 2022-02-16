from socket import fromshare
from django import forms 


class LeadForm(forms.Form):
    first_name = forms.CharField(label="First Name: ", max_length=100)
    last_name = forms.CharField(label="Last Name: ", max_length=100)
    age = forms.IntegerField(label="Age: ",min_value=0)
