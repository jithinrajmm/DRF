
from django.urls import path,include
from api import views

urlpatterns = [
        path('',views.api_views,name='api'),
        path('api/post/',views.post_view,name='api'),
        path('generic/',include('product.urls')),
    ]