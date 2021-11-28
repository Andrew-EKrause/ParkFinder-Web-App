"""
    Description:
    ...
    The urls.py file establishes the url routes that link the
    HTML pages with the views.py file for the Parks app in the 
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
from . import views
# from Parks import views # --> MAYBE THIS INSTEAD OF THE CODE ABOVE!!!
from django.urls import path

# The url patterns array contains the paths to the
# different HTML pages of the web application.
# The paths for the majority  of the pages for the 
# website are created in this file.
urlpatterns = [
    path("", views.home, name="ParkFinder-home"),
    path("home/", views.home, name="ParkFinder-home"),
    path("about/", views.about, name="ParkFinder-about"),
    path("find_parks/", views.find_parks, name="ParkFinder-find_parks"),
    path("parks/", views.parks, name="ParkFinder-parks"),
    path("specific_park/", views.specific_park, name="ParkFinder-specific_park"), # --> THIS MAY CHANGE!!! WE MAY GET RID OF IT!!!
]
