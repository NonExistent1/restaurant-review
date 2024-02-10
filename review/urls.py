from django.urls import path
from .views import RestaurantListView, RestaurantDetailView, ReviewDetailView

urlpatterns=[
    path("", RestaurantListView.as_view(), name="home"),
    path("restaurant/<int:pk>/", RestaurantDetailView.as_view(), name='restaurant_detail'),
    path("review/<int:pk>/", ReviewDetailView.as_view(), name='review_detail'),
]