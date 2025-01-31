from django.db import models
import uuid
from django.urls import reverse

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
    cover = models.ImageField(upload_to="book_covers/", blank=True, null=True)  # New field

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", args=[str(self.id)])
