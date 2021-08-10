from django.db import models
from django.urls import reverse  # use this import for making redirection

# Create your models here.


class Product(models.Model):
	name = models.CharField(max_length=250)
	description = models.CharField(max_length=500)
	price = models.PositiveIntegerField()
	image = models.FileField()

	def get_absolute_url(self):
		return reverse('waters:product', kwargs={
			'pk': self.pk})  # when you create a new product, it redirects you to the detail page of that product.

	def __str__(self):
		return self.name


class Order(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField()
	destination = models.TextField()
	delivered = models.BooleanField()
	date = models.DateTimeField(auto_now_add=True)

	def get_absolute_url(self):
		return reverse('waters:order')

	def __str__(self):
		return self.destination
