"""
    Description:
    ...
    The views.py file within the Accounts app for the project
    implements basic sign-in and sign-up protocols that enable
    a user to register for an account or login to an existing
    one. Data validation and security are important to the
    process of giving a registered user a way to access more 
    unique features of the web application.
    ...
    Project: ParkFinder Web Application
    Authors: Andrew Krause, Anthony Musbach, Gavin McCllelan
    Class: Introduction to Programming Languages (CS 224)
    Date: 12/06/2021
"""

# Create a list of imports to render the page on screen.
from django.shortcuts import render

"""
   Create the login page for the ParkFinder web
   application. The login page contains basic 
   login-protocols that the user follows to 
   login to an existing account.
"""
def login(request):
    return render(request, 'Accounts/login.html')

"""
   Create the registration page for the web application.
   The registration page is utilized by the user when 
   the user wishes to obtain an account for the website.
"""
def register(request):
    return render(request, 'Accounts/register.html')

"""
   Create the user profile page for the web application.
   This page is only accessible if the user is registered
   with the system, which means they have a valid account.
"""
def user_profile(request):
    return render(request, 'Accounts/user_profile.html')
