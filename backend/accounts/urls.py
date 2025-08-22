from django.urls import path
from .views import signup_view
from django.shortcuts import render

def signin_view(request):
    return render(request, 'signin.html')

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('signin/', signin_view, name='signin'),  # Add this line for the signin page
]