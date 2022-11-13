from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    #url('', views.home, name = 'blog-home'),
    path('', views.home, name = 'blog-home'),
    path('about/', views.about, name='blog-about'),

]