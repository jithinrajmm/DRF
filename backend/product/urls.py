from django.urls import path
from product.views import SingleProductApiView
from product import views


urlpatterns = [
    path('',views.home,name='home'),
    path('single/<int:pk>/',SingleProductApiView.as_view()),
    path('create/',views.CreateView.as_view())
    ]
