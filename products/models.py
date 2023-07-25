from django.db import models
from cloudinary.models import CloudinaryField


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
    # likes = models.ManyToManyField(Customer, related_name='product_likes', blank=True)

    def __str__(self):
        return self.item_name


class Theme(models.Model):
    theme = models.CharField(max_length=100)

    def __str__(self):
        return self.theme

    def get_absolute_url(self):
        return reverse('home')
