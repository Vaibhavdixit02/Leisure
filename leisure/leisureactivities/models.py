from __future__ import unicode_literals
from django import forms
from django.core import exceptions
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
import simplejson as json
from django.db import models

# Create your models here.
class CommentsForm(forms.Form):
	comment_content = models.CharField(max_length = 2000)
	user_name = models.CharField(max_length = 100)
		
class Comments(models.Model):
	comment_content = models.CharField(max_length = 2000)
	user_name = models.CharField(max_length = 100)
	def __str__(self):
		return str([self.user_name, self.comment_content])


class PlaceToVisitForm(forms.Form):
	link_page = models.CharField(max_length = 1000)
	link_img = models.CharField(max_length = 1000)
	user_name = models.CharField(max_length = 100)
		
class PlaceToVisit(models.Model):
	link_page = models.CharField(max_length = 1000)
	link_img = models.CharField(max_length = 1000)
	user_name = models.CharField(max_length = 100)
	def __str__(self):
		return str([self.link_page, self.link_img, self.user_name])

		
class PlaceToEatForm(forms.Form):
	link_page = models.CharField(max_length = 1000)
	link_img = models.CharField(max_length = 1000)
	user_name = models.CharField(max_length = 100)

class PlaceToEat(models.Model):
	link_page = models.CharField(max_length = 1000)
	link_img = models.CharField(max_length = 1000)
	user_name = models.CharField(max_length = 100)
	def __str__(self):
		return str([self.link_page, self.link_img, self.user_name])

class EventForm(forms.Form):
	event_date = models.CharField(max_length = 100)
	event_time = models.CharField(max_length = 100)
	event_place = models.CharField(max_length = 500)
	event_desc = models.CharField(max_length = 1000)
	user_name = models.CharField(max_length = 100)

class Events(models.Model):
	event_date = models.CharField(max_length = 100)
	event_time = models.CharField(max_length = 100)
	event_place = models.CharField(max_length = 500)
	event_desc = models.CharField(max_length = 1000)
	user_name = models.CharField(max_length = 100)
	def __str__(self):
		return str([self.event_date,self.event_time,self.event_place,self.event_desc,self.user_name])

	
		
	