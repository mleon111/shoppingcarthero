from django.http import HttpResponse
from django.shortcuts import render
from .models import Item


def index(request):
	latest_items_list = Item.objects.order_by('-pub_date')[:5]
	context = {
		'latest_items_list': latest_items_list,
	}
	return render(request, 'shop/index.html', context)

def cart(request):
	return HttpResponse("Hello from the cart view!")

def item(request, item_id):
	return HttpResponse("Hello from the item view! You're looking at item # %s" % item_id)


