from django.shortcuts import render
from django.http import *
from models import *
from django.views import View
import simplejson as jsont
from django.views.decorators.clickjacking import xframe_options_exempt
# Create your views here.

@xframe_options_exempt
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
			user_name = request.POST.get("user_name")
			item = SellModel.objects.create(item_type = item_type,item_desc = item_desc, item_img = item_img, item_costprice = item_costprice, seller_name = seller_name, seller_room = seller_room, seller_hostel = seller_hostel,seller_contact = seller_contact,user_name = user_name)
	return MainPage(request)

@xframe_options_exempt
def DeleteItem(request):
	if request.method == 'POST':
		delform = SellForm(request.POST, request.FILES)
		if delform.is_valid():
			SellModel.objects.get(item_desc = request.POST.get("item_desc"), item_costprice= request.POST.get("item_costprice"), 
				seller_name= request.POST.get("seller_name"), seller_room=request.POST.get("seller_room"), seller_hostel= request.POST.get("seller_hostel"), seller_contact=request.POST.get("seller_contact"),user_name = request.POST.get("user_name") ).delete()
	return MainPage(request)

@xframe_options_exempt
def SearchItem(request):
	if request.method == 'POST':
		finditems=SellModel.objects.filter(item_type__iexact = request.POST.get("item_type"))
		for item in finditems:
			item.item_img = str(item.item_img)[15:]
	return render(request, 'app/buysellfrontend.html', context = {"finditems" : finditems})

@xframe_options_exempt
def MainPage(request):
	all_items = SellModel.objects.all()
	for item in all_items:
		item.item_img = str(item.item_img)[15:]


	return render(request, 'app/buysellfrontend.html', context = {"all_items" : all_items})
	