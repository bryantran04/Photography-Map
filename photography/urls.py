from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('browse/', views.browse, name='browse'),
    path('contact/', views.contact, name='contact'),
]