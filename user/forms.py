from django import forms
from django.db import transaction
from django.forms.utils import ValidationError
from app.models import *
from user.models import *
from  django.contrib.auth.forms import  UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField, PasswordResetForm
from  django.contrib.auth.forms import  UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField, PasswordResetForm


class ReporterSignUpForm(UserCreationForm):
   
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=("Username"), error_messages={ 'invalid': ("This value must contain only letters, numbers and underscores.") })
    first_name = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=("Surname"))
    last_name = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=("Last Name"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=("Password (again)"))

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in [ 'username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(("The username already exists. Please try another one."))
 
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(("The two password fields did not match."))
        return self.cleaned_data



    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', )

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_reporter = True
        user.save()
        p = ReporterProfile.objects.create(user=user)
        p.save()
        return user


class ReporterProfileForm(forms.ModelForm):


    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'})) 
    

    
    class Meta:
        model = ReporterProfile
        exclude = ('updated_at', 'created_at', 'user', 'activation')



class UserChangeForm(UserChangeForm):
    
    password = ReadOnlyPasswordHashField(
        label=("Password"),
        help_text=(
            "Raw passwords are not stored, so there is no way to see this "
            "user's password, but you can change the password using "
           
           "<a href=\"passwordupdate\">this form</a>."

    
        ),
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name',)




class ReporterSocialMediaForm(forms.ModelForm):
    
    class Meta:
        model = ReporterSocialMedia
        exclude = ('updated_at', 'created_at', 'user',)


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ['user', 'created_at', 'approval', ]