from rest_framework import generics, permissions
from books.models import Book, Review
from .serializers import BookSerializer, ReviewSerializer

# ✅ API: List all books or create a new book
class BookListAPI(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # ✅ Auth required for POST

# ✅ API: Retrieve, update, or delete a single book
class BookDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # ✅ Auth required for changes

# ✅ API: List all reviews for a book
class ReviewListAPI(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """Filter reviews by book ID"""
        book_id = self.kwargs["book_id"]
        return Review.objects.filter(book_id=book_id)

    def perform_create(self, serializer):
        """Auto-assign the user to the review"""
        serializer.save(user=self.request.user)

# ✅ API: Retrieve, update, or delete a specific review
class ReviewDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
