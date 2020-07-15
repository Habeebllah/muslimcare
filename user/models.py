from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.contenttypes.fields import GenericRelation
from user.models import *

# Create your models here.
class User(AbstractUser):
    is_reporter = models.BooleanField(default=False)
    is_login = models.BooleanField(default=False)


class ReporterProfile(models.Model):
    
    GENDER = (
        ('Male', "Male"),
        ('Female', "Female"),
    )
    JOB =(
        ('Full-Time', 'Full-Time'),
        ('Part-Time', 'Part-Time'),
        ('Votuntary', 'Votuntary'),
        ('Pay-As-Your-Go', 'Pay-As-Your-Go')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job_type = models.CharField('Job Applying For?', max_length=10, choices=JOB)
    date_of_birth = models.DateField("Date of Birth", null=True)
    phone_number = models.CharField('Phone Number', max_length=25)
    gender = models.CharField('Gender', max_length=10, choices=GENDER)
    address = models.CharField("Permanent Address", max_length=250)
    identification = models.ImageField("Means of Identification", upload_to='reporter')
    image = models.ImageField("Reporter Passport", upload_to='reporter')
    about_me = models.TextField("About Me")
    activation = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.username



class ReporterSocialMedia(models.Model):

    SOCIALMEDIA = (
        ('Facebook', 'Facebook'),
        ('Twitter', 'Twitter'),
        ('Instagram', 'Instagram'),
        ('Hanghout', 'Hangout')
    )
    

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    socialmedia = models.CharField(max_length=50, choices=SOCIALMEDIA) 
    url = models.URLField("Your Url Link", max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    

    def __str__(self):
        return self.user.username
    


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=300)
    content = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    

    def __str__(self):
        return f' Sent By: {self.user} - Message Title: {self.subject}'
