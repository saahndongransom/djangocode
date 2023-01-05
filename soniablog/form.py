from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from tinymce.widgets import TinyMCE
from soniablog.models import Comment
from .models import Post
from . models import subscribers



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


    class Meta:
        fields = ('content', )


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'comment here ...',
        'rows': '4',
    }))

    class Meta:
        model = Comment
        fields = ('content', )
        

   

class PostForm(forms.ModelForm):
   class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'tags',
        ]
    

class SubscibersForm(forms.ModelForm):
    class Meta:
        model = subscribers
        fields = ['email',]
 




