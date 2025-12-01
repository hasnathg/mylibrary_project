from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list_view, name ='book_list'),
    path('about/', views.about_view, name='about'),
]