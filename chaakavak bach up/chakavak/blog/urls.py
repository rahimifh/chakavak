from django.urls import path
from . import views
app_name='blog'

urlpatterns = [
    path('', views.news, name='news'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.news_detail,name='news_detail'),

]
