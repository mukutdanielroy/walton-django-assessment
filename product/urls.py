from django.urls import path
# from django.urls import re_path
from .views import ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('api/products/', ProductListView.as_view(), name='product-list'),
    path('api/products/create/', ProductCreateView.as_view(), name='product-create'),
    path('api/products/<int:pk>/', ProductUpdateView.as_view(), name='product-update'),
    path('api/products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
]