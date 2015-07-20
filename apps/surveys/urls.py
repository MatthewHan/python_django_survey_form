__author__ = 'MatthewHan'
from django.conf.urls import patterns, url # import functions to match patterns
from apps.surveys import views
urlpatterns = [
    url(r'^process_form/', views.process_form, name = 'process_form'),
    url(r'^result/', views.result, name = 'result'),
    url(r'^$', views.index, name='index'),
]