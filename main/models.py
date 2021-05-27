from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='products/',blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
    def __str__(self):
        return self.name

class agency (models.Model):
    name = models.CharField(max_length=200)
    city =  models.CharField(max_length=200)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class apply (models.Model):
    full_name= models.CharField(max_length=50)
    email =models.CharField(max_length=150)
    phone =models.CharField(max_length=20)
    address = models.TextField(blank=True)
    text =models.TextField(blank=True)
    def __str__(self):
        return self.full_name
class slider (models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='slider/',blank=True)

    def __str__(self):
        return self.name
        
class pish (models.Model):
    full_name= models.CharField(max_length=50)
    email =models.CharField(max_length=150, blank = True)
    text =models.TextField(blank=True)
    def __str__(self):
        return self.full_name

