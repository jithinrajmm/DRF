from django.urls import path
from product.views import SingleProductApiView
from product import views


urlpatterns = [
    path('',views.home,name='home'),
    # this is the class based api calls from generics
    path('single/<int:pk>/',SingleProductApiView.as_view()),
    path('create/',views.CreateView.as_view()),
    path('list/',views.ListAll.as_view()),
    path('listANDcreate/',views.ListAllview_CreateView.as_view()),
    
    
    # this is the function based view call
    # for this we have used the api_view decorator and Response from django_restframework
    path('get_post_function/',views.product_detail_create,name = 'get_or_post'),
    path('get_post_function/<int:pk>/',views.product_detail_create,name = 'get_or_post'),
    # ☝️ this is the same url as above one but aded the pk to the url
    
    ]
