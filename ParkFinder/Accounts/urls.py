"""
    Description:
    ...
    The urls.py file establishes the url routes that link the
    HTML pages with the views.py file for the Accounts app in the 
    project. In the path() function below, the information
    appearing in the quotation marks below is the information
    that will appear in the address bar of the browser when 
    the project is open and being navigated through. After the
    path function is a second parameter that appears within the
    views.py file and is executed for that given url. The third
    parameter is a name related to the url that the HTML pages
    use to help distinguish between the different paths.
    ...
    Project: ParkFinder Web Application
    Authors: Andrew Krause, Anthony Musbach, Gavin McCllelan
    Class: Introduction to Programming Languages (CS 224)
    Date: 12/06/2021
"""

# Include imports for the urls.py file.
from Accounts import views
from django.urls import path

# The url patterns array contains the paths to the
# different HTML pages of the web application.
urlpatterns = [
    path("loginas/", views.loginas, name="ParkFinder-loginas"),
    path("register/", views.register, name="ParkFinder-register"),
    path("user_profile/", views.user_profile, name="ParkFinder-user_profile"),
]

# YOU MAY END UP DELETING THIS FILE LATER ON!!!