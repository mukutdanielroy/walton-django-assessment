from django.urls import path
from .views import PurchaseListView, PurchaseCreateView

urlpatterns = [
    path('api/purchases/', PurchaseListView.as_view(), name='purchase-list'),
    path('api/purchases/create/', PurchaseCreateView.as_view(), name='purchase-create'),
]
