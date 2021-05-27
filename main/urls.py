from django.urls import path
from . import views
app_name='main'

urlpatterns = [
    path('', views.main, name='home'),
    path('create/', views.request_apply, name='request_apply'),
    path('comments/', views.pishnahad, name='comments'),
    path('aboutus/', views.about_US, name='about'),
    path('agency/', views.agency_add, name='agencis'),
    path('products/', views.products_list, name='prod'),
    path('products/<int:product_pk>/', views.products_detail, name='detiale'),



]
