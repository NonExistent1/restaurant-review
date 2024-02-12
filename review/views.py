"""
Jordyn Kuhn
CIS 218
2-12-2024
"""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Restaurant, Review

class RestaurantListView(ListView):
    """Restaurant List View"""
    model = Restaurant
    template_name = "home.html"

class RestaurantDetailView(DetailView):
    """Restaurant Detail View"""
    model = Restaurant
    template_name = "restaurant_detail.html"

class ReviewDetailView(DetailView):
    """Review Detail View"""
    model = Review
    template_name = "review_detail.html"

class ReviewCreateView(CreateView):
    """Review Create View"""
    model = Review
    template_name = "review_new.html"
    fields = ["restaurant", "author", "rating", "body"]

    def get_initial(self):
        """Get initial form data"""
        # Get the result of calling the parent methods
        initial_data = super().get_initial()
        # Add the author so it is the requests user
        initial_data["author"] = self.request.user
        initial_data["restaurant.name"] = self.request.user
        # Return the author
        return initial_data
    
class ReviewUpdateView(UpdateView):
    """Review Update View"""
    model = Review
    template_name = "review_edit.html"
    fields = ["restaurant", "rating", "body"]

class ReviewDeleteView(DeleteView):
    """Review Delete View"""
    model = Review
    template_name = "review_delete.html"
    success_url = reverse_lazy("home")