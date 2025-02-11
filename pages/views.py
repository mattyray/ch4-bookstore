from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from .forms import ContactForm

class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class PrivacyPolicyView(TemplateView):  # This now includes Terms & Conditions
    template_name = "privacy_policy.html"

class ContactPageView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, "contact.html", {"form": form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Send email
            send_mail(
                subject=f"New Contact Form Submission: {subject}",
                message=f"Name: {name}\nEmail: {email}\n\n{message}",
                from_email=email,  # User's email
                recipient_list=['mnraynor90@gmail.com'],  # Your email
            )

            return redirect("contact_success")  # Redirect to success page

        return render(request, "contact.html", {"form": form})

class ContactSuccessView(TemplateView):
    template_name = "contact_success.html"
