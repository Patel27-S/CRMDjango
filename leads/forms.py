from socket import fromshare
from django import forms 
from .models import Lead



class LeadModelForm(forms.ModelForm):
    class Meta:
        model=Lead
        fields=(
            'first_name',
            'last_name',
            'age',
            'agent'
        )





class LeadForm(forms.Form):
    first_name = forms.CharField(label="First Name: ", max_length=100)
    last_name = forms.CharField(label="Last Name: ", max_length=100)
    age = forms.IntegerField(label="Age: ",min_value=0)
