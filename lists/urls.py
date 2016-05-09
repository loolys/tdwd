from django.conf.urls import url
from django.conf.urls.static import static

from lists import views

urlpatterns = [
    url(r'^new$', views.new_list, name='new_list'),
    url(r'^(\d+)/$', views.view_list, name='view_list'),
    #url(r'^(\d+)/new_item$', views.add_item, name='add_item'),
]

