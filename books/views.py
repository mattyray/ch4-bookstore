from django.views.generic import ListView, DetailView
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "books_list"

    def get_queryset(self):
        category = self.kwargs.get("category")
        if category:
            return Book.objects.filter(category=category)  # Now properly filters by category
        return Book.objects.all()

class BookDetailView(DetailView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"
