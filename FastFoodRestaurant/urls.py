from django.urls import path
from FastFoodRestaurant.views import *

app_name='FastFoodRestaurant'

urlpatterns = [
    path('', index_view,name='index'),
    path('about', about_view,name='about'),
    path('book', book_view,name='book'),
    path('menu', menu_view,name='menu')
]