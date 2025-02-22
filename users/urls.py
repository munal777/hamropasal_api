from django.urls import path, include
from rest_framework import routers
from .views import UserCreationAPI

router = routers.DefaultRouter()
router.register(r'register', UserCreationAPI, basename='register')

urlpatterns = [
    path('', include(router.urls))
]