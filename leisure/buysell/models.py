from __future__ import unicode_literals
from django import forms
from django.core import exceptions
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
import simplejson as json
from django.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='buysell/pictures')

class SellForm(forms.Form):
	item_type = models.CharField(max_length = 100)
	item_desc = models.CharField(max_length = 500)
	item_img = models.ImageField(upload_to = 'buysell/static/pictures')
	item_costprice = models.CharField(max_length = 50)
	seller_name = models.CharField(max_length = 50)
	seller_room = models.CharField(max_length = 20)
	seller_hostel = models.CharField(max_length = 30)
	seller_contact = models.CharField(max_length = 11)

class SellModel(models.Model):
	item_type = models.CharField(max_length = 100)
	item_desc = models.CharField(max_length = 500)
	item_img = models.ImageField(upload_to = 'buysell/static/pictures')
	item_costprice = models.CharField(max_length = 50)
	seller_name = models.CharField(max_length = 50)
	seller_room = models.CharField(max_length = 20)
	seller_hostel = models.CharField(max_length = 30)
	seller_contact = models.CharField(max_length = 11)
		

