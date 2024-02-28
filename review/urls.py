"""
Jordyn Kuhn
CIS 218
2-28-2024
"""

from django.urls import path
from .views import RestaurantDetailView, RestaurantListView, ReviewCreateView, ReviewDeleteView, ReviewDetailView, ReviewUpdateView

urlpatterns=[
    path("review/new/", ReviewCreateView.as_view(), name="review_new"),
    path("restaurant/<int:pk>/", RestaurantDetailView.as_view(), name='restaurant_detail'),
    path("review/<int:pk>/", ReviewDetailView.as_view(), name='review_detail'),
    path("review/<int:pk>/edit/", ReviewUpdateView.as_view(), name="review_edit"),
    path("review/<int:pk>/delete/", ReviewDeleteView.as_view(), name="review_delete"),
    path("", RestaurantListView.as_view(), name="home"),
]