from django.db import models

# Create your models here.
from django.contrib.auth.models import  User,Group
import datetime
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

class UserDetails(models.Model):
    
    class Role(models.TextChoices):
        Student = 'ST', _('Student')
        Faculty = 'FC', _('Faculty')

    user=models.OneToOneField(User, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=20, default='null')
    last_name=models.CharField(max_length=20, default='null')
    email=models.EmailField(max_length=50)
    role = models.CharField(max_length=2,
        choices=Role.choices,
        default=Role.Student)
    year_of_intake=models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(2017), max_value_current_year])


@receiver(post_save, sender=User)
def create_user_details(sender, instance, created, **kwargs):
    if created:
        UserDetails.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_details(sender, instance, **kwargs):
    instance.userdetails.save()
