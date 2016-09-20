from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render
from .models import Item
from django.contrib.auth.decorators import login_required


def index(request):
	latest_items_list = Item.objects.order_by('-pub_date')[:5]
	paginator = Paginator(latest_items_list, 4)
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

@login_required
def profile(request):
	profile = request.user.profile
	return render(request, 'shop/profile.html', {'profile': profile})

@login_required
def cart(request):
	return HttpResponse("Hello from the cart view!")

def item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'shop/item.html', {'item': item})


