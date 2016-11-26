from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

handler404 = views.error404
handler500 = views.error404
handler301 = views.error404

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^coupons/', include('coupons.urls', namespace='coupons')),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^orders/', include('orders.urls', namespace='orders')),
    url(r'^account/', include('account.urls')),
    url(r'^', include('shop.urls', namespace='shop')),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)