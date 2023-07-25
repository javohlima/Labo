from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('list', views.list, name='list'),
    path('sponsors', views.sponsors, name='sponsors'),
]
