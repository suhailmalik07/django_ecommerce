from django.shortcuts import render
from django.views.generic import ListView, DetailView, ListView, View, TemplateView

from .models import Item


class ItemListView(ListView):
    model = Item
    template_name = 'core/home.html'


class ItemDetailView(DetailView):
    model = Item
    template_name = 'core/product.html'


class CheckoutView(TemplateView):
    template_name = 'core/checkout.html'
