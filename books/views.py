from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Book, Review
from .forms import ReviewForm

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

    def get_context_data(self, **kwargs):
        """Pass the review form to the template"""
        context = super().get_context_data(**kwargs)
        context["form"] = ReviewForm()  # ✅ Pass the form to the template
        return context

# ✅ Restore `BookCreateView`
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

@login_required
def add_review(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            return redirect("book_detail", pk=book.pk)

    return redirect("book_detail", pk=book.pk)
