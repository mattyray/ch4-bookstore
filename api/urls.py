from django.urls import path
from .views import BookListAPI, BookDetailAPI, ReviewListAPI, ReviewDetailAPI

urlpatterns = [
    path("books/", BookListAPI.as_view(), name="book_list_api"),
    path("books/<uuid:pk>/", BookDetailAPI.as_view(), name="book_detail_api"),
    path("books/<uuid:book_id>/reviews/", ReviewListAPI.as_view(), name="review_list_api"),
    path("reviews/<int:pk>/", ReviewDetailAPI.as_view(), name="review_detail_api"),
]
