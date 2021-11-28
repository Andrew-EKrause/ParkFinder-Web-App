"""
    Description:
    ...
    The forms.py for Accounts app in the project holds a custom 
    form which is used for registering a new user. This form 
    inherits from UserCreationForm and simply adds an email field. 
    ...
    Project: ParkFinder Web Application
    Authors: Andrew Krause, Anthony Musbach, Gavin McCllelan
    Class: Introduction to Programming Languages (CS 224)
    Date: 12/06/2021
"""

# Include import statements, which include built-in functions.
from django import forms
from crispy_forms.helper import FormHelper

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

"""
    Custom form class for registering a user with the store
"""
class UserRegistrationForm(UserCreationForm):
    
    # helper = FormHelper()
    # helper.form_show_labels = False
    
    email = forms.EmailField()

    # Meta data for the form
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]