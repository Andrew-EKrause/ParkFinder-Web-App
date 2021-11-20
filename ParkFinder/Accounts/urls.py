
# Include imports for the urls.py file.
from Accounts import views
from django.urls import path

# The url patterns array contains the paths to the
# different HTML pages of the web application.
urlpatterns = [
    path("login/", views.login, name="ParkFinder-login"),
    path("register/", views.register, name="ParkFinder-register"),
    path("user_profile/", views.user_profile, name="ParkFinder-user_profile"),
]

# YOU MAY END UP DELETING THIS FILE LATER ON!!!