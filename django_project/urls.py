
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')), # new
    path('accounts/', include('allauth.urls')), # new
]
