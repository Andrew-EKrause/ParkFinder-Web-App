"""
    Author: Andrew Krause
    Description: 
        Blah blah blah...
"""

# Include imports for the urls.py file.
from . import views
# from Parks import views # --> MAYBE THIS INSTEAD OF THE CODE ABOVE!!!
from django.urls import path

# The url patterns array contains the paths to the
# different HTML pages of the web application.
urlpatterns = [
    path("", views.home, name="ParkFinder-home"),
    path("home/", views.home, name="ParkFinder-home"),
    path("about/", views.about, name="ParkFinder-about"),
    path("find_parks/", views.find_parks, name="ParkFinder-find_parks"),
    path("parks/", views.parks, name="ParkFinder-parks"),
    path("specific_park/", views.specific_park, name="ParkFinder-specific_park"), # --> THIS MAY CHANGE!!! WE MAY GET RID OF IT!!!
]
