"""
    Description:
    ...
    The views.py file within the Parks app implements an
    API obtained from the National Park Services (NPS). The 
    API allows the web application to provide data about 
    different national parks, monuments, and locations in
    all 50 states in the U.S. In addition to the use of the
    API, other pages for the site are rendered within this file.
    ...
    Project: ParkFinder Web Application
    Authors: Andrew Krause, Anthony Musbach, Gavin McCllelan
    Class: Introduction to Programming Languages (CS 224)
    Date: 12/06/2021
"""

# National Parks and Services API Key: XApMBEDd2SIXa1aX7bakVem1E28W0wWgtHuGn3SF

# Create a list of imports to render the page on screen.
from django.shortcuts import render, redirect
import requests
import pip._vendor.requests 
import urllib.request, json
from natlparks import NatlParks
from django.contrib.auth.models import User

# For now create a global variable, a list, to store the places that
# the user wants to visit in. This will be passed to the front end
# of the user profile page.
locations_list = []

"""
    Create the home page for the web application.
    The home page contains a button for the user 
    to click when they want to find parks and places
    to explore.
"""
def home(request):
    return render(request, 'Parks/pages/home.html')

"""
   Create the about page for the web application.
   The about page describes why the website was
   created as well as its uses.
"""
def about(request):
    return render(request, 'Parks/pages/about.html')

"""
   Create a find parks page for the web application  
   when the user clicks the button on the homepage.
   The page renders 50 buttons for all of the U.S.
   states on the page.
"""
def find_parks(request):
    
    # Create a list of dictionaries that stores all 50 states  
    # in the U.S. in order to pass them into the frontend.
    nps_state_list = [{"state_name": "Alabama", "state_abbreviation": "AL"},
                      {"state_name": "Alaska", "state_abbreviation": "AK"},
                      {"state_name": "Arizona", "state_abbreviation": "AZ"},
                      {"state_name": "Arkansas", "state_abbreviation": "AR"},
                      {"state_name": "California", "state_abbreviation": "CA"},

                      {"state_name": "Colorado", "state_abbreviation": "CO"},
                      {"state_name": "Connecticut", "state_abbreviation": "CT"},
                      {"state_name": "Delaware", "state_abbreviation": "DE"},
                      {"state_name": "Florida", "state_abbreviation": "FL"},
                      {"state_name": "Georgia", "state_abbreviation": "GA"},
                      
                      {"state_name": "Hawaii", "state_abbreviation": "HI"},
                      {"state_name": "Idaho", "state_abbreviation": "ID"},
                      {"state_name": "Illinois", "state_abbreviation": "IL"},
                      {"state_name": "Indiana", "state_abbreviation": "IN"},
                      {"state_name": "Iowa", "state_abbreviation": "IA"},
                      
                      {"state_name": "Kansas", "state_abbreviation": "KS"},
                      {"state_name": "Kentucky", "state_abbreviation": "KY"},
                      {"state_name": "Louisiana", "state_abbreviation": "LA"},
                      {"state_name": "Maine", "state_abbreviation": "ME"},
                      {"state_name": "Maryland", "state_abbreviation": "MD"},
                      
                      {"state_name": "Massachusetts", "state_abbreviation": "MA"},
                      {"state_name": "Michigan", "state_abbreviation": "MI"},
                      {"state_name": "Minnesota", "state_abbreviation": "MN"},
                      {"state_name": "Mississippi", "state_abbreviation": "MS"},
                      {"state_name": "Missouri", "state_abbreviation": "MO"},
                      
                      {"state_name": "Montana", "state_abbreviation": "MT"},
                      {"state_name": "Nebraska", "state_abbreviation": "NE"},
                      {"state_name": "Nevada", "state_abbreviation": "NV"},
                      {"state_name": "New Hampshire", "state_abbreviation": "NH"},
                      {"state_name": "New Jersey", "state_abbreviation": "NJ"},
                      
                      {"state_name": "New Mexico", "state_abbreviation": "NM"},
                      {"state_name": "New York", "state_abbreviation": "NY"},
                      {"state_name": "North Carolina", "state_abbreviation": "NC"},
                      {"state_name": "North Dakota", "state_abbreviation": "ND"},
                      {"state_name": "Ohio", "state_abbreviation": "OH"},
                      
                      {"state_name": "Oklahoma", "state_abbreviation": "OK"},
                      {"state_name": "Oregon", "state_abbreviation": "OR"},
                      {"state_name": "Pennsylvania", "state_abbreviation": "PA"},
                      {"state_name": "Rhode Island", "state_abbreviation": "RI"},
                      {"state_name": "South Carolina", "state_abbreviation": "SC"},
                      
                      {"state_name": "South Dakota", "state_abbreviation": "SD"},
                      {"state_name": "Tennessee", "state_abbreviation": "TN"},
                      {"state_name": "Texas", "state_abbreviation": "TX"},
                      {"state_name": "Utah", "state_abbreviation": "UT"},
                      {"state_name": "Vermont", "state_abbreviation": "VT"},
                      
                      {"state_name": "Virginia", "state_abbreviation": "VA"},
                      {"state_name": "Washington", "state_abbreviation": "WA"},
                      {"state_name": "West Virginia", "state_abbreviation": "WV"},
                      {"state_name": "Wisconsin", "state_abbreviation": "WI"},
                      {"state_name": "Wyoming", "state_abbreviation": "WY"}]
    
    # Create a variable to pass the nps_state_list to the frontend.
    state_list = {
            'statelist': nps_state_list,
    }
    
    # If the method is POST, render the information. Otherwise, still render the data.
    if request.method == "POST":
        return render(request, 'Parks/pages/find_parks.html', state_list)
    else:
        return render(request, 'Parks/pages/find_parks.html', state_list)

"""
   Create the parks list page for the web application.
   Here we utilize the National Park Services API to 
   obtain park information to display on the frontend.
   Django contains a package that enables the server to
   call to the National Park Services API and obtain the 
   data.
"""
def parks(request):

    # First use the installed django extension for the api, called natlparks.
    # A call to the API is made here.
    parks = NatlParks("XApMBEDd2SIXa1aX7bakVem1E28W0wWgtHuGn3SF")
    
    # Create a list variable to store the data 
    # returned from the api request. Obtain the
    # data from the NPS API.
    nps_data_to_parse = []
    NUMBER_OF_PLACES_IN_API = 464
    nps_data_to_parse = parks.parks(limit=NUMBER_OF_PLACES_IN_API, start=1)
    
    # Create a second list to pass to the frontend 
    # when the data from the API is obtained.
    nps_data_list = []

    # -------------------------------------------------------------------------
    # Populate a list with dictionary objects using a loop.
    # -------------------------------------------------------------------------

    # Create variables that determine the number of 
    # iterations performed by the while loop.
    # --> This should be the maximum number of places given by the NPS API.
    NUMBER_OF_PARKS = NUMBER_OF_PLACES_IN_API 
    i = 0
    
    # Create a dictionary element to store the data from the JSON file.
    # The dictionary will be added to a list of dictionary objects.
    # This dictionary is only used to access all of the data in the json
    # file.
    nps_data_dict = {}
    nps_data_dict = nps_data_to_parse['data']
    
    # The while loop analyzes the data in the JSON file 
    # returned by the API, dividing it and adding it as
    # an object of the state_park class to a list.
    while(i < NUMBER_OF_PARKS):
        
        # Obtain the packaged information for a given park/place in the JSON file.
        nps_first_element = nps_data_dict[i]
        
        # Obtain specific data attributes from the data dictionary.
        nps_id_attribute = nps_first_element['id']
        nps_name_attribute = nps_first_element['fullName']
        nps_description_attribute = nps_first_element['description']
        nps_latitude_attribute = nps_first_element['latitude']
        nps_longitude_attribute = nps_first_element['longitude']
        
        # Create data attributes for the state(s) that 
        # the national park or place is located in.
        nps_states_attribute = nps_first_element['states']
        nps_states_attribute = nps_states_attribute.split(",")
        nps_states_attribute_list = ", "
        nps_states_attribute_list = nps_states_attribute_list.join(nps_states_attribute)
        
        # Get the directions attribute to the national park or place.
        nps_directions_attribute = nps_first_element['directionsUrl']
                
        # Obtain image data from the API.
        nps_images_list = nps_first_element['images']
        nps_image_element = nps_images_list[0]
        nps_image_attribute = nps_image_element['url']
        
        # Place the obtained data in a dictionary that will
        # be passed to the frontend of the web application.
        nps_data_to_display = {}
        
        # Add a key value pair to the nps data dictionary, 
        # which is the name of the state. This action is only 
        # completed once, which is indicated by the conditional.
        if(i == 0):
            state_name = request.POST.get('state', '').strip()
            nps_data_to_display["state_name_display"] = state_name
            
            # Also add the state abbreviation, called
            # state-code, for use in the frontend. --> MAYBE DELETE LATER!!!
            state_code = request.POST.get('state-code', '').strip()
            nps_data_to_display["state_code"] = state_code
                    
        # Populate the dictionary with values to be displayed 
        # on the frontend of the website.
        nps_data_to_display["id"] = nps_id_attribute
        nps_data_to_display["fullName"] = nps_name_attribute
        nps_data_to_display["description"] = nps_description_attribute
        nps_data_to_display["latitude"] = nps_latitude_attribute
        nps_data_to_display["longitude"] = nps_longitude_attribute
        nps_data_to_display["states"] = nps_states_attribute
        nps_data_to_display["states_list"] = nps_states_attribute_list
        nps_data_to_display["directionsUrl"] = nps_directions_attribute
        nps_data_to_display["image"] = nps_image_attribute
        
        # Add the state name, for use in the frontend, to
        # every dictionary in order to perform checks. --> MAYBE DELETE LATER!!!
        state_name = request.POST.get('state', '').strip()
        nps_data_to_display["state_name"] = state_name
            
        # Also add the state abbreviation, called
        # state-code, for use in the frontend. 
        state_code = request.POST.get('state-code', '').strip()
        nps_data_to_display["state_code"] = state_code
        
        # Push the dictionary to a list that will be passed into the frontend.
        nps_data_list.append(nps_data_to_display)
        
        # Increment the counter variable.
        i += 1
        
    # -------------------------------------------------------------------------
    # End of loop used to populate list with dictionary objects.
    # -------------------------------------------------------------------------
    
    # Create a variable to pass the nps_data_list to the frontend.
    park_list = {
            'parklist': nps_data_list,
    }
    
    # If the method is a post requst, render the data for the park on 
    # screen. Otherwise, redirect to the find parks page of the website.
    if request.method == "POST":
        return render(request, 'Parks/pages/parks.html', park_list)
    else:
        return redirect("ParkFinder-find_parks")

"""
   Create a route for adding a park or place to the user profile
   page. When a user wants to add a new park or place to their
   profile, this route is activated.
"""
def add_place(request):
    
#     # If the method is a post request, check if the user is authenticated.
#     if request.method == "POST":
        
#         # If the user is authenticated, render the data on the user's profile 
#         # page. Otherwise, direct the user to the login page of the website.
#         if request.user.is_authenticated:
            
#             # Get the value of the button.
#             park_name = request.POST.get('park_name', '')
#             print(park_name)
            
#             # Check if the data from the button click was passed through.
#             # If the data was passed through, then process the data.
#             if(park_name != None):
                
#                 # Append the place that the user wants to visit to
#                 # the global variable
#                 global locations_list
#                 locations_list.append(park_name)
                
#                 # Store the data in a dictionary to be passed through.
#                 user_locations = locations_list
#                 data_to_display = {
#                     "userlocations": user_locations
#                 }
                
#                 # Render the user profile page with the data passed through.
#                 return render(request, "Accounts/pages/user_profile.html", data_to_display)
#             else:
#                 # Render the user profile page without the data passed through.
#                 return redirect("ParkFinder-user_profile")
#         else:
    return redirect("ParkFinder-loginas")

"""
   Create the specific park page for the web application.
   --> YOU MAY END UP DELETING THIS; DO NOT
   THINK YOU WILL NEED IT.
"""
def specific_park(request):
    return render(request, 'Parks/pages/specific_park.html')
