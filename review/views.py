from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Restaurant, Review

class RestaurantListView(ListView):
    """Restaurant List View"""
    model = Restaurant
    template_name = "home.html"

class RestaurantReviewListView(DetailView):
    """Review List View"""
    model = Review
    template_name = ""
