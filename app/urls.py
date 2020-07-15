from django.urls import path
from app import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('about/', views.About, name='about'),
    path('ourfunding/', views.Our_Funding, name='ourfunding'),
    path('ourproject/', views.Our_Project, name='ourproject'),
    path('contact/', views.Contact, name='contact'),
    path('faq/', views.FAQ, name='faq'),
    path('socialprotection/', views.SocialProtection, name='socialprotection'),
    path('childeducation/', views.ChildEducation, name='childeducation'),
    path('healthpromotion/', views.HealthPromotion, name='healthpromotion'),
    path('leadership/', views.Leadership, name='leadership'),
    path('marriageissue/', views.MarriageIssue, name='marriageissue'),
    path('marriagecounseling/', views.MarriageCounseling, name='marriagecounseling'),
    path('stories/', views.Stories, name='stories'),
    path('mystory/', views.Mystory, name='mystory'),
    path('opinion/', views.Opinion, name='opinion'),
    path('socialresponsibilities/', views.SocialResponsibilities, name='socialresponsibilities'),
    path('store/', views.Store, name='store'),
    path('event/', views.PostEvent, name='event'),
    path('sharestory/', views.Sharestory, name='sharestory'),
    path('reporter/', views.Reporter, name='reporter'),
    path('volunteer/', views.Volunteer, name='volunteer'),
    path('donate/', views.Donate, name='donate'),
    path('newscategory<slug:slug>', views.Newscategory, name='newscategory'),
    path('activity/', views.Activities, name='activity'),
    path('capacity/', views.Capacity, name='capacity'),
    path('social/', views.Social, name='social'),
    path('interest/', views.Interests, name='interest'),
    path('viewevents/', views.ViewEvent, name='viewevents'),
    path('eventdetails/<int:pk>/', views.EventDetails, name='eventdetails'),
    path('newsdetails/<str:pk>/', views.NewsDetails, name='newsdetails'),
    path('issuedetials/<int:pk>/', views.IssueDetails, name='issuedetails'),
    path('news', views.Newslist, name='news'),



]