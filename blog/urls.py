from django.urls import path, include
from .views import home_page, article_detail_page

urlpatterns = [
    path('', home_page, name='about'),
    path('detail/<int:pk>/', article_detail_page, name='detail'),

]
