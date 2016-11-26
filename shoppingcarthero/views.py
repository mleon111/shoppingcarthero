from django.http import HttpResponse

from django.template import loader

def error404(request):
     template = loader.get_template('404.html')
     #context = Context({'message': 'All: %s' % request,})
     return HttpResponse(content=template.render(), content_type='text/html; charset=utf-8', status=404)

def index(request):
    return HttpResponse("Hello, world. You are in the homepage view!")