from django.urls import path
from .views import BookListView, BookDetailView

urlpatterns = [
    path("", BookListView.as_view(), name="book_list"),
    path("<uuid:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("category/<str:category>/", BookListView.as_view(), name="book_category"),  # Ensures proper filtering
]
