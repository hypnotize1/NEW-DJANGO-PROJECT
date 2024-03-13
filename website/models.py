from django.db import models
from phonenumber_field .modelfields import PhoneNumberField
from django.core.validators import RegexValidator

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField()
    subject = models.CharField(max_length = 255, blank = True, null = True)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['created_date']
    
    def __str__(self):
        return self.name


class Quote(models.Model):
    name = models.CharField(max_length=100, help_text='Enter your name')
    email = models.EmailField(max_length=254, help_text='Enter your email address')
    phone_regex = RegexValidator(
        regex=r'^\+98\d{10}$',
        message='Phone number must start with +98 and have 10 digits.'
    )
    phone_number = PhoneNumberField(validators=[phone_regex], blank=True, help_text='Enter your phone number')
    message = models.TextField(help_text='Enter your message')
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['created_date']

    
    def __str__(self):
        return self.name
