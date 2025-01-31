from django.views.generic import ListView, DetailView  # ✅ Import DetailView
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books_list'

class BookDetailView(DetailView):  # ✅ Fix: Use DetailView instead of ListView
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'  # ✅ This ensures that the template uses "book"
