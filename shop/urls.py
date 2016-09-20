from django.conf.urls import url

from . import views

app_name = 'shop'
urlpatterns = [
    # ex: /shop/
    url(r'^$', views.index, name='index'),
    # ex: /shop/5/
    url(r'^(?P<item_id>[0-9]+)/$', views.item, name='item'),
    # ex: /shop/cart/
    url('cart/', views.cart, name='cart'),
    # ex: /shop/profile/
    url('profile/', views.profile, name='profile'),
]