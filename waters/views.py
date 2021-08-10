from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Product, Order
from django.views import generic
from django.views.generic import View, TemplateView
from .forms import OrderForm

# Create your views here.


class IndexView(generic.ListView):
	template_name = 'waters/index.html'
	context_object_name = "first_five"

	def get_queryset(self):
		return Product.objects.all()[:5]


class DetailView(generic.DetailView):
	model = Product
	template_name = "waters/product.html"


class ProductsView(generic.ListView):
	template_name = 'waters/shop.html'
	context_object_name = "products"
	model = Product


class MakeOrder(CreateView):
	model = Order
	fields = ['product', 'quantity', 'destination']


class Contact(TemplateView):
	template_name = 'waters/contact.html'
