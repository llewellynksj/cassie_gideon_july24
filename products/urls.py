from django.urls import path
from . import views

urlpatterns = [
    path('', views.CategoryList.as_view(), name='home'),
    path('products/', views.ProductList.as_view(), name='products'),
    path('product/<int:pk>', views.ProductDetails.as_view(), name='product_details'),
    path('like/<int:pk>', views.LikeView, name='like_post'),
    path('category/<str:cats>/', views.CategoryView, name='category',)
]
