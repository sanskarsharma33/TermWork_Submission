from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserDetails
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

class ProfileForm(forms.ModelForm):
    #first_name=forms.CharField(max_length=20)
    #last_name=forms.CharField(max_length=20)
    #email=forms.EmailField(max_length=50)
    #role=forms.CharField(max_length=1)
    #year_of_intake=forms.IntegerField()
    #profile_picture=forms.ImageField(required=False)
    class Meta:
        model=UserDetails
        fields=('first_name', 'last_name','email', 'year_of_intake')