from django.contrib import admin
from .models import Book, Review

class ReviewInline(admin.TabularInline):  
    model = Review
    extra = 1  # Allow adding reviews directly from the book admin page

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "price", "category", "cover_preview")
    inlines = [ReviewInline]  # Embed reviews in the book admin page

    def cover_preview(self, obj):
        if obj.cover:
            return f'<img src="{obj.cover.url}" width="50">'
        return "No Image"
    cover_preview.allow_tags = True
    cover_preview.short_description = "Cover"

admin.site.register(Book, BookAdmin)
admin.site.register(Review)
