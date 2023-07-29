from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class Category(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    category_image = CloudinaryField('image', default='placeholderproduct')
    category_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    main_image = CloudinaryField('image', default='placeholder')
    item_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(default="", null=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=50)
    description = models.TextField(default='placeholder', blank=True, max_length=1000)
    colours = models.TextField(default='Ivory', blank=True, max_length=500)
    sizes_avail = models.TextField(default='Enquire in store', blank=True, max_length=500)
    favourites = models.ManyToManyField(User, related_name='favourite', blank=True)

    def __str__(self):
        return self.item_name


class Theme(models.Model):
    theme = models.CharField(max_length=100)

    def __str__(self):
        return self.theme

    def get_absolute_url(self):
        return reverse('home')
