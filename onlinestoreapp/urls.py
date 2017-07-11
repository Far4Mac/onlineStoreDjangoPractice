from django.conf.urls import url
from views import ProductDetail, Products_in_category, Products

urlpatterns = [
    url(r'^$', Products.as_view(), name='ProductList'),
    url(r'^(?P<category_slug>[-\w]+)/$', Products_in_category.as_view(), name='ProductsInCategory'),
    url(r'^(?P<pk>[0-9]+)/(?P<slug>[-\w]+)/$', ProductDetail.as_view(), name='ProductDetail')
]