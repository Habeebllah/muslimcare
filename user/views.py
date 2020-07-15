from django.contrib import messages
from django.contrib.auth import login as mylogin
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.http.response import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView, TemplateView
from django.contrib.auth.forms import PasswordChangeForm
from .decorators import *
from user.forms import *
from user.models import *
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as django_logout
from django.contrib import  auth, messages
from app.forms import *
from app.models import *
from django.core.mail import send_mail


from django.conf import settings
User = settings.AUTH_USER_MODEL


class Confirmation(TemplateView):
    template_name = 'confirmation.html'


class ReporterSignUpView(CreateView):
    model = User
    form_class = ReporterSignUpForm
    template_name = 'registration/signup_form.html'

 
    def form_valid(self, form):
        user = form.save()
        mylogin(self.request, user)
        p = ReporterProfile.objects.get(user=self.request.user.id)
        return redirect('updateprofile', p.id)

def UpdateProfile(request, pk):
    template_name = 'updateprofile.html'
    logo = Logo.objects.filter().first()
    reporter = get_object_or_404(ReporterProfile, pk=pk)
    form = ReporterProfileForm(request.POST or None, request.FILES or None, instance = reporter)
    if request.method == 'POST':
        if form.is_valid():
            p = form.save(commit=False)
            p.save()
            messages.success(request, 'You Application Was Successfully Submitted Check Back Within 24 hours')
            return redirect('confirmation')
    return render(request, template_name, {'form': form, 'logo': logo,})

def login(request):
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            if form.is_valid():
                user = auth.authenticate(username=username, password=password)

                if user is not None:
                    auth.login(request, user)

                    
                    if request.user.is_reporter and request.user.is_login == False:
                        messages.success(request, 'You Application is still under processing, We will Update you as soon as possible!')
                        return redirect('mylogin')
                    elif request.user.is_reporter:
                        return redirect('dashboard')

                             
            
            else:
                args = {'form': form}
                return render(request, 'registration/login.html', args)

        else:
            form = AuthenticationForm

        logo = Logo.objects.filter().first()
        args = {'form': form, 'logo': logo,}
        return render(request, 'registration/login.html', args)


def logout_user(request):
    django_logout(request)
    return HttpResponseRedirect('/')

@reporter_required
def Dashboard(request):
    template_name = 'administrator/dashboard.html'
    logo = Logo.objects.filter().first()
    post = News.objects.filter(user=request.user).order_by('-created_at')
    approval_counts = News.objects.filter(user=request.user, approval=True).count()
    awaitingapproval_counts = News.objects.filter(user=request.user, approval=False).count()
    post_counts = News.objects.filter(user=request.user).count()
    publish_counts = News.objects.filter(user=request.user, status='Published').count()
    draft_counts = News.objects.filter(user=request.user, status='Draft').count()
    message_counts = Message.objects.filter(user=request.user).count()


    context = {
        'message_counts': message_counts,
        'approval_counts': approval_counts,
        'post_counts': post_counts, 
        'publish_counts': publish_counts,
        'draft_counts': draft_counts,
        'post': post,
        'awaitingapproval_counts': awaitingapproval_counts,
        'logo': logo,

    }
    return render(request, template_name, context)

@reporter_required
def Addpost(request):
    form = NewsForm()
    #print(request.user.email)
    logo = Logo.objects.filter().first()
    
    if request.method == 'POST':
        form = NewsForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            p = form.save(commit=False)
            p.user = request.user
            p.save()
            send_mail(f'{request.user.first_name} {request.user.last_name} just added a new post title: {p.title}', 'Kindly check you admin to verify', 'lasisihabeeb67@gmail.com', ['lasisihabeebllah@gmail.com'], fail_silently=False)
            messages.success(request, 'You Blog Has Been Successfully Submitted')
            return redirect('dashboard')
    template_name = 'administrator/addpost.html'
    return render(request, template_name, {'form': form, 'logo': logo,})

@reporter_required
def EditPost(request, pk):
    logo = Logo.objects.filter().first()
    template_name = 'administrator/editpost.html'
    post = get_object_or_404(News, pk=pk)
    form = NewsForm(request.POST or None, request.FILES or None, instance = post)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'You Blog Has Been Successfully Submitted')
            return redirect('viewpost')
    return render(request, template_name, {'form': form, 'logo': logo,})

@reporter_required
def Viewpost(request):
    template_name = 'administrator/viewpost.html'
    logo = Logo.objects.filter().first()
    post = News.objects.filter(user=request.user)
    return render(request, template_name, {'post': post, 'logo': logo,})


@reporter_required
def Editprofile(request, pk):
    template_name = 'administrator/editprofile.html'
    reporter = get_object_or_404(ReporterProfile, pk=pk)
    logo = Logo.objects.filter().first()
    form = ReporterProfileForm(request.POST or None, request.FILES or None, instance = reporter)
    if request.method == 'POST':
        if form.is_valid():
            p = form.save(commit=False)
            p.save()
            messages.success(request, 'You Application will be taken into consideration under 24 hours')
            return redirect('dashboard')
    return render(request, template_name, {'form': form, 'logo': logo,})


@reporter_required
def Addsocialmedia(request):
    template_name = 'administrator/addsocialmedia.html'
    logo = Logo.objects.filter().first()
    return render(request, template_name, {'logo': logo,})


@reporter_required
def Viewsocialmedia(request):
    template_name = 'administrator/viewsocialmedia.html'
    logo = Logo.objects.filter().first()
    return render(request, template_name, {'logo': logo,})


@reporter_required
def Settings(request):
    template_name = 'administrator/settings.html'
    logo = Logo.objects.filter().first()
    return render(request, template_name, {'logo': logo,})


@reporter_required
def Updatepassword(request):
    template_name = 'administrator/updatepassword.html'
    logo = Logo.objects.filter().first()
    return render(request, template_name, {'logo': logo,})


@reporter_required
def Settings(request):
    logo = Logo.objects.filter().first()
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        #profile_form = ProfileForm(request.POST, instance=request.user.profile)
        #if user_form.is_valid() and profile_form.is_valid():
        if form.is_valid():
            form.save()
            #profile_form.save()
            messages.error(request, 'The Details has been Updated Successfully.')
            return redirect('dashboard')
        else:
            #print(user_form.errors, profile_form.errors)
            print(form.errors)

    elif request.method == "GET":
        form = UserChangeForm(instance=request.user)
        #profile_form = ProfileForm(instance=request.user.profile)
        #return render(request, 'user_data.html', {'user_form': user_form, 'profile_form': profile_form})
        return render(request, 'accountdetails.html', {'form': form, 'logo': logo,})



@reporter_required
def change_password(request):
    logo = Logo.objects.filter().first()
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form, 'logo': logo,})


@reporter_required
def Addsocialmedia(request):
    logo = Logo.objects.filter().first()
    form = ReporterSocialMediaForm()
    if request.method == 'POST':
        form = ReporterSocialMediaForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            p = form.save(commit=False)
            p.user = request.user
            p.save()
            messages.success(request, 'Your Post Has Been Successfully Submitted')
            return redirect('dashboard')
    template_name = 'administrator/addsocialmedia.html'
    return render(request, template_name, {'form': form, 'logo': logo,})



@reporter_required
def Viewsocialmedia(request):
    template_name = 'administrator/viewsocialmedia.html'
    post = ReporterSocialMedia.objects.filter(user=request.user)
    return render(request, template_name, {'post': post,})

@reporter_required
def delete_social_media(request, pk):
    post = ReporterSocialMedia.objects.get(id=pk).delete()
    return redirect('viewsocialmedia')


@reporter_required
def Updatesocialmedia(request, pk):
    template_name = 'administrator/updatesocialmedia.html'
    post = get_object_or_404(ReporterSocialMedia, pk=pk)
    form = ReporterSocialMediaForm(request.POST or None, request.FILES or None, instance = post)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Update Was Successfully Submitted')
            return redirect('viewsocialmedia')
    return render(request, template_name, {'form': form, 'post': post,})


@reporter_required
def Viewpostpublished(request):
    template_name = 'administrator/postpublished.html'
    post = News.objects.filter(user=request.user, status='Published')
    return render(request, template_name, {'post': post})


@reporter_required
def Viewpostdraft(request):
    template_name = 'administrator/postdraft.html'
    post = News.objects.filter(user=request.user, status='Draft')
    return render(request, template_name, {'post': post})


@reporter_required
def Viewpostawaitingapproval(request):
    template_name = 'administrator/postawaitingapproval.html'
    post = News.objects.filter(user=request.user, approval=False)
    return render(request, template_name, {'post': post})


@reporter_required
def Viewpostapproved(request):
    template_name = 'administrator/postapproved.html'
    post = News.objects.filter(user=request.user, approval=True)
    return render(request, template_name, {'post': post})


@reporter_required
def Sendmessage(request):
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            p = form.save(commit=False)
            p.user = request.user
            p.save()
            messages.success(request, 'You Message Has Been Sent Successfully')
            return redirect('viewmessage')
    template_name = 'administrator/sendmessage.html'
    return render(request, template_name, {'form': form})


@reporter_required
def Viewsentmessages(request):
    template_name = 'administrator/viewsentmessages.html'
    message = Message.objects.filter(user=request.user)
    return render(request, template_name, {'message': message,})


@reporter_required
def Deletemessage(request, pk):
    message = Message.objects.get(id=pk).delete()
    return redirect('viewmessage')


@reporter_required
def Updatemessage(request, pk):
    template_name = 'administrator/updatemessage.html'
    message = get_object_or_404(Message, pk=pk).order_by('-created_at')
    form = MessageForm(request.POST or None, request.FILES or None, instance = message)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Message Was Updated Successfully')
            return redirect('viewmessage')
    return render(request, template_name, {'form': form, 'message': message,})


@reporter_required
def Receivedmessage(request):
    template_name = 'administrator/receivedmessage.html'
    message = Message.objects.filter(user=request.user)
    return render(request, template_name, {'message': message,})    


@reporter_required
def Messagecount(request):
    template_name = 'header.html'
    message_counts = Message.objects.filter(user=request.user).count()
    return render(request, template_name, {'message_counts': message_counts,})