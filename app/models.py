from django.db import models
from django.contrib.auth.models import User
from app.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.contenttypes.fields import GenericRelation
from user.models import *
from ckeditor_uploader.fields import RichTextUploadingField
#from ckeditor.fields import RichTextField
# Create your models here.


class Top_Quote(models.Model):
    firstline = models.TextField(max_length=2000)
    secondline = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Top_Quote'
        verbose_name_plural = 'Top_Quote'

    def __str__(self):
        return f'{self.firstline} {self.secondline}'

class Services(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return f'{self.title}'

class Activity(models.Model):
    title = models.CharField(max_length=50)
    headline = models.TextField(max_length=1000)
    content = RichTextUploadingField(max_length=1000000)
    image = models.ImageField(upload_to='app')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activity'

class MarriageCheckUp(models.Model):
    title = models.CharField(max_length=50)
    headline = models.TextField(max_length=1000)
    content = RichTextUploadingField(max_length=1000000)
    image = models.ImageField(upload_to='app')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Marriage Check Up'
        verbose_name_plural = 'Marriage Check Up'


class SocialResponsibility(models.Model):
    title = models.CharField(max_length=50)
    headline = models.TextField(max_length=1000)
    content = RichTextUploadingField(max_length=1000000)
    image = models.ImageField(upload_to='app')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Social Responsibility'
        verbose_name_plural = 'Social Responsibility'

class Interest(models.Model):
    title = models.CharField(max_length=50)
    headline = models.TextField(max_length=1000)
    content = RichTextUploadingField(max_length=1000000)
    image = models.ImageField(upload_to='app')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Interest'
        verbose_name_plural = 'Interest'

class Advert(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='app')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

class Sponsor(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='app')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    name = models.CharField("Category", max_length=50)
    slug = models.SlugField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'News Category'
        verbose_name_plural = 'News Categories'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name}'


class News(models.Model):
    STATUS = (
        ('Published', 'Published'),
        ('Draft', 'Draft'),

    )

    POST_TYPE = (
        ('Video', 'Video'),
        ('Audio', 'Audio'),
        ('Text', 'Text'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    content = RichTextUploadingField(max_length=1000000)
    post_type = models.CharField(max_length=10, choices=POST_TYPE)
    image = models.ImageField(upload_to='app')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    url = models.URLField("Video URLs (If video post)", blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS)
    approval = models.BooleanField(default=False)
    slug = models.SlugField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Posted By: {self.user} - Post Title: {self.title} - Post Category: {self.category.name}'


    def get_absolute_url(self):
        return reverse('postdetails', args=[self.slug])

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'


class Comment(models.Model):
    post = models.ForeignKey(News, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    fullname = models.CharField('Full Name', max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.fullname}'

    class Meta:
        verbose_name = 'News Comment'
        verbose_name_plural = 'News Comments'


class Sharestory(models.Model):

    POST_TYPE = (
        ('Video', 'Video'),
        ('Audio', 'Audio'),
        ('Text', 'Text'),
    )

    full_name = models.CharField(max_length=200)
    title = models.CharField(max_length=1000)
    story = models.TextField(max_length=10000)
    post_type = models.CharField(max_length=10, choices=POST_TYPE)
    image = models.ImageField(upload_to='app')
    url = models.URLField("Video URLs (If video post)", blank=True, null=True)
    approval = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return f' Sent By: {self.full_name} - Story Title: {self.title}'

    class Meta:
        verbose_name = 'Share your story'
        verbose_name_plural = 'Share your stories'

class Logo(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='app')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class Event(models.Model):
    event_theme = models.CharField(max_length=500)
    organization = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    speaker = models.CharField('speaker(s)', max_length=500)
    event_description = models.TextField(max_length=5000)
    venue = models.CharField(max_length=2000)
    target_audience = models.CharField(max_length=5000)
    duration = models.CharField(max_length=50)
    approval = models.BooleanField(default=False)
    date_and_time_of_event = models.DateTimeField('Date and Time of Event', null=True)
    image = models.ImageField('Event Poster', upload_to='app')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.organization} -- {self.event_theme} -- {self.date_and_time_of_event} -- Contact: {self.phone_number}'



class MarriageCounseling(models.Model):
    SEX = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

   
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=SEX)
    age = models.IntegerField()
    years_of_marriage = models.IntegerField()
    state_of_origin = models.CharField(max_length=400)
    LGA = models.CharField(max_length=200)
    nature_of_conflict = models.TextField(max_length=5000)
    contact = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.name}'


class FrontBanner(models.Model):
    image = models.ImageField(upload_to='app')
    firstline = models.CharField(max_length=200)
    secondline = models.CharField(max_length=500)
    button = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.firstline}'

class MarriageIssues(models.Model):
    title = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='app')
    nature_of_conflict = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Marriage Issue'
        verbose_name_plural = 'Marriage Issues'

class MarriageComment(models.Model):
    issue = models.ForeignKey(MarriageIssues, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    fullname = models.CharField('Full Name', max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.fullname}'

    class Meta:
        verbose_name = 'Marriage Issues Comment'
        verbose_name_plural = 'Marriage Issues Comments'


class Volunteer(models.Model):
    SEX = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField( max_length=100)
    email = models.EmailField(max_length=254)
    phonenumber = models.CharField(max_length=20)
    gender = models.CharField(max_length=50, choices=SEX)
    address = models.TextField(max_length=1000)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} -- {self.last_name}'

    class Meta:
        verbose_name = 'Volunteer'
        verbose_name_plural = 'Volunteers'

class FooterTexts(models.Model):
    heading = models.CharField(max_length=50)
    content = models.TextField(max_length=20000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.heading}'

    class Meta:
        verbose_name = 'Footer Text'
        verbose_name_plural = 'Footer Texts'

class Newsletter(models.Model): 
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'

class BaseWords(models.Model):
    words = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.words}'

    class Meta:
        verbose_name = 'Base Words'
        verbose_name_plural = 'Base Words'