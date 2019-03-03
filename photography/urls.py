from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('search/results', views.results, name='results'),
    path("<int:location_id>/profile/", views.profile, name='profile'),
]