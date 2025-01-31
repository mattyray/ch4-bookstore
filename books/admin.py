from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "price", "category", "cover_preview")  # Show cover in admin

    def cover_preview(self, obj):
        if obj.cover:
            return f'<img src="{obj.cover.url}" width="50">'
        return "No Image"
    cover_preview.allow_tags = True
    cover_preview.short_description = "Cover"

admin.site.register(Book, BookAdmin)
