
from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^addcomment/$',views.AddComment, name = 'addcomment'),
	url(r'^addplacetovisit/$',views.AddPlaceToVisit, name = 'addplacetovisit'),
	url(r'^addplacetoeat/$',views.AddPlaceToEat, name = 'addplacetoeat'),
	url(r'^addevent/$',views.AddEvent, name = 'addevent'),
	url(r'^mainpage/$',views.MainPage, name = 'mainpage'),
	url(r'^showcomment/$',views.ShowComment, name = 'showcomment'),
	url(r'^showevent/$',views.ShowEvent, name = 'showevent'),
	url(r'^showvisit/$',views.ShowVisit, name = 'showvisit'),
	url(r'^showeat/$',views.ShowEat, name = 'showeat'),
	url(r'^delcomment/$',views.DelComment, name = 'delcomment'),
	url(r'^delevent/$',views.DelEvent, name = 'delevent'),
	url(r'^delvisit/$',views.DelVisit, name = 'delvisit'),
	url(r'^deleat/$',views.DelEat, name = 'deleat'),
]