from django import forms
from myApp.models import Contact, Newsletter
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from captcha.fields import CaptchaField

class NameForm(forms.Form):
    name=forms.CharField(max_length=255)
    email=forms.EmailField()
    subject=forms.CharField(max_length=255)
    message=forms.CharField(widget=forms.Textarea)

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model=Contact
        fields='__all__'
        """
        widgets = {
            'message':SummernoteWidget(),
        }
        """


class NewsletterForm(forms.ModelForm):
    class Meta:
        model=Newsletter
        fields='__all__'

