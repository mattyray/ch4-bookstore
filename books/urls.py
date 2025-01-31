from django.urls import path
from .views import (
    BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView
)

urlpatterns = [
    path("", BookListView.as_view(), name="book_list"),
    path("<uuid:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("add/", BookCreateView.as_view(), name="book_add"),
    path("<uuid:pk>/edit/", BookUpdateView.as_view(), name="book_edit"),
    path("<uuid:pk>/delete/", BookDeleteView.as_view(), name="book_delete"),
    path("category/<str:category>/", BookListView.as_view(), name="book_category"),
]
