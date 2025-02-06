from rest_framework import serializers
from books.models import Book, Review

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "author", "price", "category", "cover"]

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # ✅ Show username instead of ID

    class Meta:
        model = Review
        fields = ["id", "book", "user", "content", "rating", "created_at"]
