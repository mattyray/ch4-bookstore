from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3, "class": "form-control", "placeholder": "Write your review..."}),
        label=""
    )

    class Meta:
        model = Review
        fields = ["content"]
