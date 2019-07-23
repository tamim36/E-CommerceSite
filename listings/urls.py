from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('categories/<categoryName>/' , views.category , name = 'category'),
    path('search', views.search, name='search'),
]
