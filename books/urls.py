from django.urls import path
from .views import (
    BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView, SearchResultsListView, add_review
)

urlpatterns = [
    path("", BookListView.as_view(), name="book_list"),
    path("<uuid:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("<uuid:pk>/review/", add_review, name="add_review"),
    path("add/", BookCreateView.as_view(), name="book_add"),
    path("<uuid:pk>/edit/", BookUpdateView.as_view(), name="book_edit"),
    path("<uuid:pk>/delete/", BookDeleteView.as_view(), name="book_delete"),
    path("category/<str:category>/", BookListView.as_view(), name="book_category"),
    path("search/", SearchResultsListView.as_view(), name="search_results"),
]


