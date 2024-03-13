from django import forms
from website.models import Contact, Quote
from captcha.fields import CaptchaField

class contact_form(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'


class QuoteForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Quote
        fields = ['name', 'message', 'phone_number', 'email']