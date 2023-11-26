
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name='home'),
    path('about', views.about,name='about product'),
    path('signup', views.signup,name='sign'),
    path('contact', views.contact,name='contact for us'),
]
