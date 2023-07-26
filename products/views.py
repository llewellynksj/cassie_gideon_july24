from django.shortcuts import render
from django.views import generic
from .models import Category, Product, Theme
from django.contrib import messages


class CategoryList(generic.ListView):
    model = Category
    template_name = 'home.html'


class ProductList(generic.ListView):
    model = Product
    template_name = 'products.html'


# def home(request):
#     return render(request, 'home.html', {})
