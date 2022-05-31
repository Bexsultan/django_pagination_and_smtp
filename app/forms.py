from django import forms
from .models import Email
from django.forms import TextInput, Textarea, EmailInput
from django import forms

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['mail']
        widgets = {
            'mail' : EmailInput(attrs={
                'name':'mail',
                'class':'form-control',
                'placeholder':'Enter your email..'

            })
        }