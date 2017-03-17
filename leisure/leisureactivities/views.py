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

def ShowComment(request):
	if request.method == 'POST':
		user_name = request.POST.get('user_name')
	all_places_eat = PlaceToEat.objects.all()
	all_places = PlaceToVisit.objects.all()
	all_comments = Comments.objects.all()
	all_events = Events.objects.all()
	comments = Comments.objects.filter(user_name = user_name)
	return render(request, 'app/leisurefrontend.html', context = {"comments" : comments, "all_places_eat" : all_places_eat, "all_places" : all_places, "all_comments" : all_comments, "all_events" : all_events})

def ShowEvent(request):
	if request.method == 'POST':
		user_name = request.POST.get('user_name')
	all_places_eat = PlaceToEat.objects.all()
	all_places = PlaceToVisit.objects.all()
	all_comments = Comments.objects.all()
	all_events = Events.objects.all()
	events = Events.objects.filter(user_name = user_name)
	#events = str([eventu.event_time, eventu.event_date, eventu.event_place, eventu.event_desc])
	return render(request, 'app/leisurefrontend.html', context = {"events" : events, "all_places_eat" : all_places_eat, "all_places" : all_places, "all_comments" : all_comments, "all_events" : all_events})

def ShowVisit(request):
	if request.method == 'POST':
		user_name = request.POST.get('user_name')
	all_places_eat = PlaceToEat.objects.all()
	all_places = PlaceToVisit.objects.all()
	all_comments = Comments.objects.all()
	all_events = Events.objects.all()
	visits = PlaceToVisit.objects.filter(user_name = user_name)
	return render(request, 'app/leisurefrontend.html', context = {"visits" : visits, "all_places_eat" : all_places_eat, "all_places" : all_places, "all_comments" : all_comments, "all_events" : all_events})

def ShowEat(request):
	if request.method == 'POST':
		user_name = request.POST.get('user_name')
	all_places_eat = PlaceToEat.objects.all()
	all_places = PlaceToVisit.objects.all()
	all_comments = Comments.objects.all()
	all_events = Events.objects.all()
	eats = PlaceToEat.objects.filter(user_name = user_name)
	return render(request, 'app/leisurefrontend.html', context = {"eats" : eats, "all_places_eat" : all_places_eat, "all_places" : all_places, "all_comments" : all_comments, "all_events" : all_events})

def DelComment(request):
	if request.method == 'POST':
		user_name = request.POST.get('user_name')
		comment_content = request.POST.get('comment_content')
		Comments.objects.filter(user_name = user_name, comment_content = comment_content).delete()
	return MainPage(request)

def DelEvent(request):
	if request.method == 'POST':
		user_name = request.POST.get('user_name')
		event_date = request.POST.get('event_date')
		event_time = request.POST.get('event_time')
		event_place = request.POST.get('event_place')
		Events.objects.filter(user_name = user_name, event_date = event_date, event_time = event_time, event_place = event_place).delete()
	return MainPage(request)

def DelVisit(request):
	if request.method == 'POST':
		user_name = request.POST.get('user_name')
		link_img = request.POST.get('link_img')
		PlaceToVisit.objects.filter(user_name = user_name, link_img = link_img).delete()
	return MainPage(request)

def DelEat(request):
	if request.method == 'POST':
		user_name = request.POST.get('user_name')
		link_img = request.POST.get('link_img')
		PlaceToEat.objects.filter(user_name = user_name, link_img = link_img).delete()
	return MainPage(request)


def MainPage(request):
	all_places_eat = PlaceToEat.objects.all()
	all_places = PlaceToVisit.objects.all()
	all_comments = Comments.objects.all()
	all_events = Events.objects.all()
	return render(request, 'app/leisurefrontend.html', context = {"all_places_eat" : all_places_eat, "all_places" : all_places, "all_comments" : all_comments, "all_events" : all_events})
	