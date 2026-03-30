from django.contrib import admin
from django.urls import path
from Products.views import index, product_detail, category_products, add_to_cart, cart_view, remove_from_cart, bestsellers 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('category/<int:id>/', category_products, name='category_products'),
    path('product/<int:id>/', product_detail, name='product_detail'),
    path('cart/', cart_view, name='cart'),
    path('add-to-cart/<int:id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:id>/', remove_from_cart, name='remove_from_cart'),
    path('bestsellers/', bestsellers, name='bestsellers')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)