from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

class UserDetails(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=20, default='null')
    last_name=models.CharField(max_length=20, default='null')
    email=models.EmailField(max_length=50)
    role=models.CharField(max_length=1)
    year_of_intake=models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(2017), max_value_current_year])

    def set_details(self, request):
        self.first_name=request.POST.get('first_name')
        self.last_name=request.POST.get('last_name')
        self.email=request.POST.get('email')
        self.year_of_intake=request.POST.get('year_of_intake')
        self.save()


@receiver(post_save, sender=User)
def create_user_details(sender, instance, created, **kwargs):
    if created:
        UserDetails.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_details(sender, instance, **kwargs):
    instance.userdetails.save()