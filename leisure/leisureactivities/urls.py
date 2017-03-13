
from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^addcomment/$',views.AddComment, name = 'addcomment'),
	url(r'^addplacetovisit/$',views.AddPlaceToVisit, name = 'addplacetovisit'),
	url(r'^addplacetoeat/$',views.AddPlaceToEat, name = 'addplacetoeat'),
	url(r'^addevent/$',views.AddEvent, name = 'addevent'),
	url(r'^mainpage/$',views.MainPage, name = 'mainpage'),


]