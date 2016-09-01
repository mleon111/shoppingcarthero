from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You are in the index view!")

def cart(request):
	return HttpResponse("Hello from the cart view!")

def item(request, item_id):
	return HttpResponse("Hello from the item view! You're looking at item # %s" % item_id)


