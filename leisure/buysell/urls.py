
from django.conf.urls import url

from . import views

urlpatterns = [ url(r'^sellform/$', views.AddItem, name = 'sellform'),
				url(r'^mainpage/$', views.MainPage, name = 'mainpage'),
				url(r'^deleteform/$', views.DeleteItem, name= 'deleteform'),
				url(r'^searchitem/$', views.SearchItem, name= 'searchitem'),

]