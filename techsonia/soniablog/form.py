from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from tinymce.widgets import TinyMCE


def should_be_empty(value):
    if value:
        raise forms.ValidationError('Field is not empty')



class ContactForm(forms.Form):
    
    name = forms.CharField(max_length=80)
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    forcefield = forms.CharField()
    #required=(False, widget='forms.HiddenInput',label= "Leave empty", validators=[should_be_empty])
    required = forms.CharField( required=False, 
    widget=forms.HiddenInput,
    label="Leave empty",
    validators=[should_be_empty]
)


class NewsletterForm(forms.Form):
    subject = forms.CharField()
    receivers = forms.CharField()
    message = forms.CharField(widget=TinyMCE(), label="Email content")
    


  




