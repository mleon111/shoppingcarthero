from django.conf.urls import url

from django.conf.urls.static import static
from . import views
handler404 = views.error404
handler500 = views.error404
handler301 = views.error404

app_name = 'shop'
urlpatterns = [
    url(r'^$', views.item_list, name='item_list'),
    url(r'^(?P<category_slug>[-\w]+)/$',
    	views.item_list,
    	name='item_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
    	views.item_detail,
    	name='item_detail'),
]