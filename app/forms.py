from django import forms
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class NewsForm(forms.ModelForm):

    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        exclude = ['created_at', 'updated_at', 'slug', 'approval', 'user']

class ShareStoryForm(forms.ModelForm):


    class Meta:
        model = Sharestory
        exclude = ['created_at', 'updated_at', 'approval']

    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post', 'created_at',]

class MarriageCommentForm(forms.ModelForm):
    class Meta:
        model = MarriageComment
        exclude = ['issue', 'created_at', ]


class EventForm(forms.ModelForm):

        
    date_and_time_of_event = forms.DateTimeField(
        input_formats = ['%Y-%m-%dT%H:%M'],
        widget = forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'class': 'form-control'},
            format='%Y-%m-%dT%H:%M')
    )


 

    class Meta:
        model = Event
        exclude = ['created_at', 'approval', 'updated_at']

class MarriageCounselingForm(forms.ModelForm):


    class Meta:
        model = MarriageCounseling
        exclude = ['created_at', 'updated_at']


class VolunteerForm(forms.ModelForm):

    class Meta:
        model = Volunteer
        exclude = ['created_at', 'updated_at']

class ActivityForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Activity
        exclude = ['created_at', 'updated_at']

class InterestForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    
    class Meta:
        model = Interest
        exclude = ['created_at', 'updated_at']

class MarriageCheckUpForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    
    class Meta:
        model = MarriageCheckUp
        exclude = ['created_at', 'updated_at']

class SocialResponsibilityForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    
    class Meta:
        model = SocialResponsibility
        exclude = ['created_at', 'updated_at']

class FooterTextsForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    
    class Meta:
        model = FooterTexts
        exclude = ['created_at', 'updated_at']

class NewsletterForm(forms.ModelForm):
    email = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Email Address...'}))
    class Meta:
        model = Newsletter
        # widgets = {
        #     'email': forms.TextInput(attrs={'placeholder': 'email', 'label': ''}),
        # }
        exclude = ['created_at', 'updated_at']


class BaseWordsForm(forms.ModelForm):
    class Meta:
        model = BaseWords
        exclude = ['created_at', 'updated_at']