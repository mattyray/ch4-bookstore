from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3, "class": "form-control", "placeholder": "Write your review..."}),
        label=""
    )
    rating = forms.ChoiceField(
        choices=Review.STAR_RATINGS,
        widget=forms.Select(attrs={"class": "form-select"}),  # ✅ Bootstrap dropdown
        label="Rating"
    )

    class Meta:
        model = Review
        fields = ["content", "rating"]  # ✅ Include rating field
