from django.urls import path
from . import views
app_name='main'

urlpatterns = [
    path('', views.main, name='home'),
    path('products/', views.products_list, name='prod'),
    path('products/<int:product_pk>/', views.products_detail, name='detiale'),


]
