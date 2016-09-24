from django.conf.urls import url

from . import views

app_name = 'shop'
urlpatterns = [
    # ex: /shop/
    url(r'^$', views.item_list, name='item_list'),
    url(r'^(?P<category_slug>[-\w]+)/$',
    	views.item_list,
    	name='item_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
    	views.item_detail,
    	name='item_detail'),
    # ex: /shop/profile/
    url('profile/', views.profile, name='profile'),
]