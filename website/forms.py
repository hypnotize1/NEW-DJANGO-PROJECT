from django import forms

from website.models import Contact
from captcha.fields import CaptchaField

class contact_form(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'