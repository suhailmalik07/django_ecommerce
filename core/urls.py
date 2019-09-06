from django.urls import path

from .views import ItemListView, CheckoutView, ItemDetailView


app_name = 'core'

urlpatterns = [
    path('', ItemListView.as_view(), name='home'),
    path('product/<int:pk>/<slug>/', ItemDetailView.as_view(), name='product'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
]
