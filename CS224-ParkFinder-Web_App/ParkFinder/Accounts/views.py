
from django.shortcuts import render

# Create your views here.

# Create the login page for the web application.
def login(request):
    return render(request, 'Accounts/login.html')

# Create the registration page for the web application.
def register(request):
    return render(request, 'Accounts/register.html')

# Create the user profile page for the web application.
def user_profile(request):
    return render(request, 'Accounts/user_profile.html')
