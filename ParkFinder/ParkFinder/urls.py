"""ParkFinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Include imports for the urls.py file.
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from Accounts import views as userviews

# The url patterns array contains the paths to the
# different HTML pages of the web application.
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("Parks.urls")),
    path("", include("Accounts.urls")),
    path("register/", userviews.register, name="register_user"),
    path("login/", auth_views.LoginView.as_view(template_name="Accounts/login.html"), name="login"), # --> STILL NEED TO FIX THIS!!!
    path("logout/", auth_views.LogoutView.as_view(template_name="Accounts/logout.html"), name="logout"), # --> STILL NEED TO FIX THIS!!!
]
