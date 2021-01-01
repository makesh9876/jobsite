from django.urls import path, include
from .import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('', views.index,name='index'),
    path('home',views.index, name='home'),
    path('job_details/<slug:slug>',views.job_details,name='job_details'),
    path('search',views.search, name='search'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('login',views.login, name='login'),
    path('register',views.register, name='register'),
    path('rr',views.rr,name='rr'),
    path('message',views.message,name='message'),
    path('logout', views.logout, name='logout'),
    path('privacy',views.privacy, name='privacy'),
    path('terms',views.terms, name='terms'),

   
   
   
     
     

    ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)