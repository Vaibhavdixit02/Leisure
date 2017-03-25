from django.shortcuts import render
from django.http import *
from models import *
from django.views import View
import simplejson as json
# Create your views here.

def AddItem(request):
	if request.method == 'POST':
		sellform = SellForm(request.POST, request.FILES)
		if sellform.is_valid():
			item_type = request.POST.get("item_type")
			item_desc = request.POST.get("item_desc")
			item_img = request.FILES.get("item_img")
			item_costprice = request.POST.get("item_costprice")
			seller_name = request.POST.get("seller_name")
			seller_room = request.POST.get("seller_room")
			seller_hostel = request.POST.get("seller_hostel")
			seller_contact = request.POST.get("seller_contact")
			item = SellModel.objects.create(item_type = item_type,item_desc = item_desc, item_img = item_img, item_costprice = item_costprice, seller_name = seller_name, seller_room = seller_room, seller_hostel = seller_hostel,seller_contact = seller_contact)
	return MainPage(request)

def DeleteItem(request):
	if request.method == 'POST':
		delform = SellForm(request.POST, request.FILES)
		if delform.is_valid():
			SellModel.objects.get(item_desc = request.POST.get("item_desc"), item_costprice= request.POST.get("item_costprice"), 
				seller_name= request.POST.get("seller_name"), seller_room=request.POST.get("seller_room"), seller_hostel= request.POST.get("seller_hostel"), seller_contact=request.POST.get("seller_contact") ).delete()
	return MainPage(request)

def SearchItem(request):
	if request.method == 'POST':
		finditems=SellModel.objects.filter(item_type = request.POST.get("item_type"))
	return render(request, 'app/buysellfrontend.html', context = {"finditems" : finditems})

def MainPage(request):
	all_items = SellModel.objects.all()
	for item in all_items:
		item.item_img = str(item.item_img)[15:]


	return render(request, 'app/buysellfrontend.html', context = {"all_items" : all_items})
	