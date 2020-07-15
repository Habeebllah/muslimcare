from django.shortcuts import render, get_object_or_404, redirect
from app.models import *
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from app.forms import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.mail import send_mail

# Create your views here.

def Index(request):
    frontbanner = FrontBanner.objects.all().order_by('-created_at')[:3]
    activity = Activity.objects.filter().first()
    latest_news = News.objects.filter(status = 'Published', approval=True).order_by('-created_at')
    capacity = MarriageCheckUp.objects.filter().first()
    social = SocialResponsibility.objects.filter().first()
    interest = Interest.objects.filter().first()
    sponsor = Sponsor.objects.all().order_by('created_at')
    advert = Advert.objects.all().order_by('-created_at')[:5]
    single_event = Event.objects.filter(approval=True).first()
    event = Event.objects.filter(approval=True)[:5]
    baseword = BaseWords.objects.filter().first()
    
    form = NewsletterForm() 
    if request.method == 'POST':
        form = NewsletterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('index') 

    template_name = 'app/index.html'
    context = {
        'activity': activity,
        'capacity': capacity,
        'social': social,
        'interest': interest,
        'sponsor': sponsor,
        'latest_news': latest_news,
        'frontbanner': frontbanner,
        'advert': advert,
        'event': event,
        'single_event': single_event,
        'form': form,
        'baseword': baseword,
 
    }
    return render(request, template_name, context)

def About(request):
    template_name = 'app/about.html'
    return render(request, template_name)

def Our_Funding(request):
    template_name = 'app/ourfunding.html'
    return render(request, template_name)

def Our_Project(request):
    template_name = 'app/ourproject.html'
    return render(request, template_name)

def Contact(request):
    template_name = 'app/contact.html'
    return render(request, template_name)

def FAQ(request):
    template_name = 'app/faq.html'
    return render(request, template_name)

def SocialProtection(request):
    template_name = 'app/socialprotection.html'
    return render(request, template_name)

def ChildEducation(request):
    template_name = 'app/childeducation.html'
    return render(request, template_name)

def HealthPromotion(request):
    template_name = 'app/healthpromotion.html'
    return render(request, template_name)

def Leadership(request):
    template_name = 'app/leadership.html'
    return render(request, template_name)


def MarriageIssue(request):
    template_name = 'app/marriageissue.html'
    issues = MarriageIssues.objects.all()
    paginator = Paginator(issues, 6)  # Show 6 events per page
    page = request.GET.get('page')
    post = paginator.get_page(page)
    return render(request, template_name, {'post': post,})

def IssueDetails(request, pk):
    template_name = 'app/issuedetails.html'
    issues = MarriageIssues.objects.filter()
    marriageissue = get_object_or_404(MarriageIssues, pk=pk)
    comment = MarriageIssues.objects.get(pk=marriageissue.id)
    comments = MarriageComment.objects.filter(issue=marriageissue).order_by('-created_at')
    comment_counts = MarriageComment.objects.filter(issue=marriageissue).count()
    form = MarriageCommentForm() 
    if request.method == 'POST':
        form = MarriageCommentForm(request.POST, request.FILES)
        if form.is_valid():
            b = form.save(commit=False)
            b.issue = comment
            b.save()
        return redirect('index') 
    return render(request, template_name, {'marriageissue': marriageissue, 'form': form, 'comments': comments, 'comment_counts': comment_counts,})

def MarriageCounseling(request):
    template_name = 'app/marriagecounseling.html'
    form = MarriageCounselingForm() 
    if request.method == 'POST':
        form = MarriageCounselingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('index')
    context = {
        'form': form,
    }
    return render(request, template_name, context)

def Stories(request):
    template_name = 'app/stories.html'
    return render(request, template_name)

def Mystory(request):
    template_name = 'app/mystory.html'
    return render(request, template_name)

def Opinion(request):
    template_name = 'app/opinion.html'
    return render(request, template_name)

def Religion(request):
    template_name = 'app/religion.html'
    return render(request, template_name)

def SocialResponsibilities(request):
    template_name = 'app/socialresponsibilities.html'
    return render(request, template_name)

def PostEvent(request):
    template_name = 'app/event.html'  
    form = EventForm() 
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('index')

    context = {
        'form': form,
    }
    return render(request, template_name, context)


def ViewEvent(request):
    template_name = 'app/eventview.html'
    event = Event.objects.filter(approval=True)
    paginator = Paginator(event, 6)  # Show 6 events per page
    page = request.GET.get('page')
    events = paginator.get_page(page)

    context = {
        'events': events,
    }
    return render(request, template_name, context)

def EventDetails(request, pk):
    template_name = 'app/eventdetails.html'
    events = get_object_or_404(Event, pk=pk)
    
    context = {
        'events': events,
    }
    return render(request, template_name, context)

def Store(request):
    template_name = 'app/store.html'
    return render(request, template_name)

def Sharestory(request):
    template_name = 'app/sharestory.html'
    form = ShareStoryForm() 
    if request.method == 'POST':
        form = ShareStoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('index')

    context = {
        'form': form,
    }
    return render(request, template_name, context)

def Reporter(request):
    template_name = 'app/reporter.html'
    return render(request, template_name, context)

    
def Volunteer(request):
    template_name = 'app/volunteer.html'
    form = VolunteerForm() 
    if request.method == 'POST':
        form = VolunteerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, template_name, context)

def Donate(request):
    template_name = 'app/Donate.html'
    return render(request, template_name)

def Newscategory(request, slug):
    template_name = 'app/newscategory.html'
    newscategory = get_object_or_404(Category, slug=slug)
    posts = News.objects.filter(category=newscategory, status='Published', approval=True)
    news_category = Category.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 6)  # Show 6 events per page
    page = request.GET.get('page')
    post = paginator.get_page(page)

    context = {
        'news_category': news_category,
        'newscategory': newscategory,
        'post': post,
    }
 
    return render(request, template_name, context)

def Activities(request):
    template_name = 'app/activity.html'
    activity = Activity.objects.filter().first()
    context = {
        'activity': activity,
    }
    return render(request, template_name, context)


def Capacity(request):
    template_name = 'app/capacity.html'
    marriage = MarriageCheckUp.objects.filter().first()
    context = {
        'marriage': marriage,
    }
    return render(request, template_name, context)


def Social(request):
    template_name = 'app/social.html'
    social = SocialResponsibility.objects.filter().first()
    context = {
        'social': social,
    }
    return render(request, template_name, context)


def Interests(request):
    template_name = 'app/interest.html'
    interest = Interest.objects.filter().first()
    context = {
        'interest': interest,
    }
    return render(request, template_name, context)

def NewsDetails(request, pk):
    template_name = 'app/newsdetails.html'
    news = get_object_or_404(News, pk=pk)
    newscategory = get_object_or_404(Category, pk=pk)
    post = News.objects.filter(category=newscategory, status='Published', approval=True)
    news_category = Category.objects.all().order_by('-created_at')
    reporter = ReporterProfile.objects.get(user=news.user)  
    comments = Comment.objects.filter(post=news).order_by('-created_at')
    comment_counts = Comment.objects.filter(post=news).count()
    myblog = News.objects.get(pk=news.id)
    form = CommentForm() 
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            b = form.save(commit=False)
            b.post = myblog
            b.save()
        return redirect('index') 


    context = {
        'news_category': news_category,
        'newscategory': newscategory,
        'post': post,
        'news': news,
        'reporter': reporter,
        'comments': comments,
        'comment_counts': comment_counts,
        'form': form,
    }
 
    return render(request, template_name, context)

def Newslist(request):
    template_name = 'app/newslist.html'
    posts = News.objects.filter(status = 'Published', approval=True).order_by('-created_at')
    paginator = Paginator(posts, 6)  # Show 6 events per page
    page = request.GET.get('page')
    post = paginator.get_page(page)

    context = {
        'post': post,
    }
 
    return render(request, template_name, context)


