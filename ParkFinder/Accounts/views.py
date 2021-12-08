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
    Authors: Andrew Krause, Anthony Musbach, Gavin McClellan
    Class: Introduction to Programming Languages (CS 224)
    Date: 12/06/2021
"""

# Create a list of imports to render the page on screen.
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

"""
   Create the login page for the ParkFinder web
   application. The login page contains basic 
   login-protocols that the user follows to 
   login to an existing account.
"""
def loginas(request):
    if request.method == 'POST':
        # gathers entered information
        username = request.POST.get('username-field')
        password = request.POST.get('password-field')
        # checks that a user with the username and password entered exists
        user = authenticate(username=username, password=password)
        
        if user != None:
            login(request, user)
            return render(request, 'Accounts/user_profile.html')
        else:
            messages.error(request, 'Incorrect Username or Password')

    return render(request, 'Accounts/loginas.html')

"""
   Create the registration page for the web application.
   The registration page is utilized by the user when 
   the user wishes to obtain an account for the website.
"""
def register(request):
    if request.method == 'POST':
        # gets all the entered user information
        fname = request.POST.get('firstname-field')
        lname = request.POST.get('lastname-field')
        email = request.POST.get('email-field')
        username = request.POST.get('username-field')
        password = request.POST.get('password-field')
        passwordconf = request.POST.get('passwordconf-field')

        # checks that all fields have been filled out and checks that username and email have not already been used.
        if fname == None or lname == None or email == None or username == None or password == None or passwordconf == None:
            messages.error(request, 'A field was left Empty')
        else:
            if User.objects.filter(username=username):
                messages.error(request, "Username already exists. Please try another username")
            elif User.objects.filter(email=email):
                messages.error(request, "Email is already registered. Please try another email")
            else:
                # Checks that the two passwords entered match
                if password == passwordconf:
                    # creates a new user in the database with the entered information and returns user to home page
                    new_user = User.objects.create_user(username, email, password)
                    new_user.first_name = fname
                    new_user.last_name = lname
                    new_user.save()
                    messages.success(request, 'Your Account has been Successfully Created')

                    return redirect("ParkFinder-loginas")
                else:
                    messages.error(request, 'Passwords Do Not Match')

    return render(request, 'Accounts/register.html')

"""
   Create the user profile page for the web application.
   This page is only accessible if the user is registered
   with the system, which means they have a valid account.
"""
def user_profile(request):
    return render(request, 'Accounts/user_profile.html')
