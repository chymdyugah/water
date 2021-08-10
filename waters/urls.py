from django.conf.urls import url
from . import views

app_name = "waters"

urlpatterns = [
	# /waters/
	url(r'^$', views.IndexView.as_view(), name='index'),
	# waters/product/pk
	url(r'^product/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='product'),
	# waters/products/
	url(r'^products/$', views.ProductsView.as_view(), name='products'),
	# waters/order/
	url(r'^order/$', views.MakeOrder.as_view(), name='order'),
	# waters/contact/
	url(r'^contact/$', views.Contact.as_view(), name='contact'),
]
