from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.

def book_list_view(request):
    books = Book.objects.all()

    context ={
        'all_books': books
    }
    return render(request, 'library/book_list.html', context)

def about_view(request):
    return HttpResponse("<h1>About us</h1>")

