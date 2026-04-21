from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def home_redirect(request):
    return redirect('/api/signin/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_redirect),
    path('api/', include('accounts.urls')),  # This line includes all URLs from accounts app
]