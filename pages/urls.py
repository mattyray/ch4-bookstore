from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, PrivacyPolicyView, ContactSuccessView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('contact/success/', ContactSuccessView.as_view(), name='contact_success'),
    path('privacy-policy/', PrivacyPolicyView.as_view(), name='privacy_policy'),
]
