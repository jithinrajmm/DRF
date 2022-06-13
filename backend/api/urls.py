from unicodedata import name
from django.urls import path
from api import views

urlpatterns = [
        path('api/',views.api_views,name='api'),
    ]