from django.shortcuts import render
from .models import Author, Book

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})
from django.shortcuts import render

# Create your views here.
