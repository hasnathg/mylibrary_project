from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),

    path('books/', views.BookListView.as_view(), name ='book_list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),

    path('about/', views.about_view, name='about'),

    path('suggest-book',views.BookSuggestionCreateView.as_view(), name ='suggest_book'),
    path('suggest-book/thanks/', views.suggestion_thanks_view, name= 'suggest_thanks'),
]