from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('onlinestoreapp:ProductsInCategory', args=[self.slug])

class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='images')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('onlinestoreapp:ProductDetail', args=[self.id, self.slug])