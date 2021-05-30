from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone_number = PhoneNumberField(region="PL", blank=True, null=True)

    def __str__(self):
        return self.first_name
