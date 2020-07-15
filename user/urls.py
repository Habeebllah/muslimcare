from django.urls import path
from user import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/signup/reporter/', views.ReporterSignUpView.as_view(), name='reporter_signup'),
    path('logout', views.logout_user, name='user_logout'),
    path("login", views.login, name='mylogin'),
    path('updateprofile/<pk>', views.UpdateProfile, name='updateprofile'),
    path('confirm', views.Confirmation.as_view(), name='confirmation'),
    path('dashboard', views.Dashboard, name='dashboard'),
    path('addpost', views.Addpost, name='addpost'),
    path('viewpost', views.Viewpost, name='viewpost'),
    path('editpost/<pk>', views.EditPost, name='editpost'),
    path('editprofile/<pk>', views.Editprofile, name='editprofile'),
    path('addsocialmedia', views.Addsocialmedia, name='addsocialmedia'),
    path('viewsocialmedia', views.Viewsocialmedia, name='viewsocialmedia'),
    path('settings', views.Settings, name='settings'),
    path('updatepassword', views.Updatepassword, name='updatepassword'),
    path('passwordupdate', views.change_password, name='password'),
    path('logindetails', views.Settings, name='userdetails'),
    path('updatesocialmedia/<pk>', views.Updatesocialmedia, name='updatesocialmedia'),
    path('deletesocialmedia/<pk>/', views.delete_social_media, name='deletesocialmedia'),
    path('postapproved', views.Viewpostapproved, name='postapproved'),
    path('postawaitingapproval', views.Viewpostawaitingapproval, name='postawaitingapproval'),
    path('postpublished', views.Viewpostpublished, name='postpublished'),
    path('postdraft', views.Viewpostdraft, name='postdraft'),
    path('sendmessage', views.Sendmessage, name='sendmessage'),
    path('viewmessage', views.Viewsentmessages, name='viewmessage'),
    path('receivedmessage', views.Receivedmessage, name='receivedmessage'),
    path('deletemessage/<pk>', views.Deletemessage, name='deletemessage'),
    path('updatemessage/<pk>', views.Updatemessage, name='updatemessage'),

]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)