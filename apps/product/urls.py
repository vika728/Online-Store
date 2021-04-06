from django.urls import path

from apps.product.views import *

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('products/products_list/', ProductListView.as_view(), name='products-list'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category-detail'),
    path('products/detail/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/edit/', ProductEditView.as_view(), name='product-edit'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='product-delete'),
    path('products/review/', ReviewIndexPage.as_view(), name='review-list'),
]