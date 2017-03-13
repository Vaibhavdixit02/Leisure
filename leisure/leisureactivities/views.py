from django.shortcuts import render
from django.http import *
from models import *
from django.views import View
import simplejson as json
# Create your views here.

vari = []	
		
def AddComment(request):
	if request.method == 'POST':
		form = CommentsForm(request.POST)
		if form.is_valid():
			comment_content = request.POST.get('comment_content')
    		user_name = request.POST.get('user_name')
    		Comment = Comments.objects.create(comment_content = comment_content, user_name = user_name)
    	return MainPage(request)
    	

def AddPlaceToVisit(request):
	if request.method == 'POST':
		form = PlaceToVisitForm(request.POST)
		if form.is_valid():
			link_page = request.POST.get('link_page')
			link_img = request.POST.get('link_img')
			Place = PlaceToVisit.objects.create(link_page = link_page, link_img = link_img)
	return MainPage(request)


def AddPlaceToEat(request):
	if request.method == 'POST':
		form = PlaceToEatForm(request.POST)
		if form.is_valid():
			link_page = request.POST.get('link_page')
			link_img = request.POST.get('link_img')
			Place = PlaceToVisit.objects.create(link_page = link_page, link_img = link_img)
	return MainPage(request)

def AddEvent(request):
	if request.method == 'POST':
		form = EventForm(request.POST)
		if form.is_valid():
			event_date = request.POST.get('event_date') 
			event_time = request.POST.get('event_time')
			event_place = request.POST.get('event_place')
			event_desc = request.POST.get('event_desc')
			Event = Events.objects.create(event_date = event_date, event_time = event_time, event_place = event_place, event_desc = event_desc)
	return MainPage(request)	


def MainPage(request):
	all_places_eat = PlaceToEat.objects.all()
	all_places = PlaceToVisit.objects.all()
	all_comments = Comments.objects.all()
	all_events = Events.objects.all()
	return render(request, 'app/webpage.html', context = {"all_places_eat" : all_places_eat, "all_places" : all_places, "all_comments" : all_comments, "all_events" : all_events})
	

	
		
	
	