from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render
from .models import Category, Item
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from cart.forms import CartAddItemForm


def item_list(request, category_slug=None):
	category = None
	categories = Category.objects.all()
	items = Item.objects.filter(available=True)
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		items = items.filter(category=category)
	paginator = Paginator(items, 4)
	page = request.GET.get('page')
	try:
		items = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		items = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		items = paginator.page(paginator.num_pages)
	return render(request, 
				  'shop/item_list.html', 
				  {'category': category,
				   'categories': categories,
				   'items': items})

def item_detail(request, id, slug):
    item = get_object_or_404(Item, 
    						 id=id,
    						 slug=slug,
    						 available=True)
    cart_item_form = CartAddItemForm()
    return render(request, 
    			  'shop/item.html', 
    			  {'item': item,
    			  'cart_item_form': cart_item_form})



