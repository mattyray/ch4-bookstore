from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from .models import Book

# ✅ Only logged-in users can view books
class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "books_list"

    def get_queryset(self):
        category = self.kwargs.get("category")
        if category:
            return Book.objects.filter(category=category)
        return Book.objects.all()

class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"

# ✅ Only users with "can_edit_books" permission can edit/delete books
class BookCreateView(PermissionRequiredMixin, CreateView):
    model = Book
    fields = ["title", "author", "price", "category", "cover"]
    template_name = "books/book_form.html"
    permission_required = "books.can_edit_books"

class BookUpdateView(PermissionRequiredMixin, UpdateView):
    model = Book
    fields = ["title", "author", "price", "category", "cover"]
    template_name = "books/book_form.html"
    permission_required = "books.can_edit_books"

class BookDeleteView(PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = "books/book_confirm_delete.html"
    success_url = reverse_lazy("book_list")
    permission_required = "books.can_edit_books"
