from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Category, Product, Theme
from products.models import Product
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse


def LikeView(request, pk):
    product = get_object_or_404(Product, id=request.POST.get('product_id'))
    liked = False
    if product.likes.filter(id=request.user.id).exists():
        product.likes.remove(request.user)
        liked = False
    else:
        product.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('product_details', args=[str(pk)]))


def CategoryView(request, cats):
    category_products = Product.objects.filter(category=cats)
    return render(request, 'categories.html', {'cats': cats, 'category_products': category_products})


class CategoryList(generic.ListView):
    model = Category
    template_name = 'home.html'


class ProductList(generic.ListView):
    model = Product
    template_name = 'products.html'


class ProductDetails(generic.DetailView):
    model = Product
    template_name = 'product_details.html'
