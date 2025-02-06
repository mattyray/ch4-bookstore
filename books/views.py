from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Book, Review
from .forms import ReviewForm
from django.db.models import Q  # Import Q for advanced filtering

class SearchResultsListView(ListView):
    model = Book
    template_name = "books/search_results.html"
    context_object_name = "book_list"

    def get_queryset(self):
        query = self.request.GET.get("q")  # Get the search term from the request
        if query:
            return Book.objects.filter(
                Q(title__icontains=query) | Q(author__icontains=query)
            )
        return Book.objects.none()  # Return no results if no query is entered

 

# ✅ Only logged-in users can view books
class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "books_list"

    def get_queryset(self):
        """Optimize book listing retrieval"""
        category = self.kwargs.get("category")
        queryset = Book.objects.all()  # Removed select_related("author")
        if category:
            return queryset.filter(category=category)
        return queryset


    
class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"

    def get_queryset(self):
        """Optimize query without using select_related on a non-relational field"""
        return Book.objects.only("title", "price", "category", "cover").prefetch_related("reviews__user")

    def get_context_data(self, **kwargs):
        """Pass the review form and optimized reviews"""
        context = super().get_context_data(**kwargs)
        context["form"] = ReviewForm()  # ✅ Pass the form to the template
        context["reviews"] = self.object.reviews.all()  # ✅ Avoid extra DB queries in template
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
    user = request.user  # ✅ Cache user to avoid duplicate queries

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = user  # ✅ Use cached user
            review.rating = form.cleaned_data["rating"]
            review.save()
            return redirect("book_detail", pk=book.pk)

    return redirect("book_detail", pk=book.pk)

@login_required
def add_review(request, pk):
    book = get_object_or_404(Book, pk=pk)
    user = request.user  # ✅ Cache user to avoid duplicate queries

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = user  # ✅ Use cached user
            review.rating = form.cleaned_data["rating"]
            review.save()
            return redirect("book_detail", pk=book.pk)

    return redirect("book_detail", pk=book.pk)

