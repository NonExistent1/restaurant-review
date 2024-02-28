"""
Jordyn Kuhn
CIS 218
2-28-2024
"""

from django.db import models
from django.urls import reverse

class Review(models.Model):
    """Review model class"""

    restaurant = models.ForeignKey(
        "Restaurant",
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    body = models.TextField()
    rating = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)

    def __str__(self):
        """String Method"""
        return self.body
    
    def get_absolute_url(self):
        return reverse("review_detail", kwargs={"pk": self.pk})

class Restaurant(models.Model):
    name = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)

    def __str__(self):
        """String Method"""
        return self.name
    
    def get_absolute_url(self):
        """Get the absolute URL for a single restaurant"""
        return reverse("restaurant_detail", kwargs={"pk": self.pk})