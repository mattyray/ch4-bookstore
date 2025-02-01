from django.db import models
import uuid
from django.urls import reverse
from django.conf import settings  # ✅ Import settings to get custom user model

class Book(models.Model):
    CATEGORY_CHOICES = [
        ("fiction", "Fiction"),
        ("nonfiction", "Nonfiction"),
        ("children", "Children's Books"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="fiction")
    cover = models.ImageField(upload_to="book_covers/", blank=True, null=True)

    class Meta:
        permissions = [
            ("can_edit_books", "Can edit books"),  # Custom permission
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", args=[str(self.id)])

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # ✅ Fixed
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} on {self.book.title}"
