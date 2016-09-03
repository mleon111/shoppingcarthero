from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Item


def index(request):
	latest_items_list = Item.objects.order_by('-pub_date')[:5]
	paginator = Paginator(latest_items_list, 4) # Show 25 contacts per page
	page = request.GET.get('page')

	try:
		items = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		items = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		items = paginator.page(paginator.num_pages)

	return render(request, 'shop/index.html', {'items': items})

def cart(request):
	return HttpResponse("Hello from the cart view!")

def item(request, item_id):
	return HttpResponse("Hello from the item view! You're looking at item # %s" % item_id)


