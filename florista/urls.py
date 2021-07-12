from django.urls import path
from florista import views

urlpatterns = [


    path('' , views.categories , name= "categories" ),
    path('' , views.home , name= "home" ),
    path('categories/' , views.categories , name= "all_categories"),
    path('categories/<pk>' , views.show_categories , name="show_categories"),
    path('cart', views.cart_details, name="cart_details"),
    path('cart/<pk>' , views.add_to_cart , name="add_to_cart"),
    path('cart/<pk>/delete' , views.delete_from_cart , name = "delete_from_cart"), 
    path('collect', views.collect_from_store, name = "collect_from_store")

    
    ]
