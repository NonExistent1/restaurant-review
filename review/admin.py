"""
Jordyn Kuhn
CIS 218
2-12-2024
"""

from django.contrib import admin

from .models import Restaurant, Review

admin.site.register(Restaurant)
admin.site.register(Review)
