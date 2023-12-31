# forms.py
from django import forms
from .models import ContactUs


class InputForm(forms.Form):
    user_input = forms.CharField(
        label='Prompt your query here..', 
        max_length=200, 
        widget=forms.TextInput(attrs={'class': 'large-input', 'row':5,'style': 'width: 90%; height: 50px;'})
    )


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'subject', 'message']