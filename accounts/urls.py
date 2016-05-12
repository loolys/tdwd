from django.conf.urls import patterns, url

from accounts import views

urlpatterns = [
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),   
]

