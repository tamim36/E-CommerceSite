from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
    path('manager', views.order_manager, name='order_manager'),
    path('<int:order_id>/', views.order_detail, name='order_detail')
    #url(r'^manager/$', views.order_manager, name='order_manager'),
]