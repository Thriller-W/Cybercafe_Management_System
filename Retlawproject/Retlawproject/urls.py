"""
URL configuration for Retlawproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import CustomerViewSet, ComputerViewSet, GameViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'computers', ComputerViewSet)
router.register(r'games', GameViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

