from django.conf.urls import url
from views import CartDetail, CartRemove, CartAdd


urlpatterns = [
    url(r'^detail/$', CartDetail.as_view(), name='CartDetail'),
    url(r'^remove/(?P<product_id>\d+)/$', CartRemove.as_view(), name='CartRemove'),
    url(r'^add/(?P<product_id>\d+)/$', CartAdd.as_view(), name='CartAdd')
]