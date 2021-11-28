"""
    Author: Andrew Krause
    Description:
        Blah blah blah...
"""

# National Parks and Services API Key: XApMBEDd2SIXa1aX7bakVem1E28W0wWgtHuGn3SF

# Create a list of imports to render the page on screen.
from django.shortcuts import render, redirect
import requests
import pip._vendor.requests 
import urllib.request, json
from natlparks import NatlParks

"""
    Create the home page for the web application.
"""
def home(request):
    return render(request, 'Parks/pages/home.html')

"""
   Create the about page for the web application.
"""
def about(request):
    return render(request, 'Parks/pages/about.html')

"""
   Create a find parks page for the web application  
   when the user clicks the button on the homepage.
"""
def find_parks(request):
    
    if request.method == "POST":
        return render(request, 'Parks/pages/find_parks.html')
    else:
        return render(request, 'Parks/pages/find_parks.html')

"""
   Create the parks list page for the web application.
   Here we utilize the National Park Services API to 
   obtain park information to display on the frontend.
"""
def parks(request):
    
    # -------------------------------------------------------------------------
    # NOTE: Here we use the National Park Services (NPS) API to obtain all of
    # the parks a selected state. WE MAY WANT TO ADD THIS OUTSIDE OF VIEWS
    # SO WE DO NOT EXCEED OUR LIMIT OF 1,000 REQUESTS PER HOUR TO THE NPS API.
    # -------------------------------------------------------------------------

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
    NUMBER_OF_PARKS = NUMBER_OF_PLACES_IN_API # --> THIS SHOULD BE THE MAXIMUM NUMBER OF PLACES IN THE FINAL VERSION OF THE PROJECT!!!
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
        nps_states_attribute = nps_first_element['states']
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
            state_name = request.POST["state"].strip()
            nps_data_to_display["state_name_display"] = state_name
            
            # Also add the state abbreviation, called
            # state-code, for use in the frontend. --> MAYBE DELETE LATER!!!
            state_code = request.POST["state-code"].strip()
            nps_data_to_display["state_code"] = state_code
        
        # Populate the dictionary with values to be displayed 
        # on the frontend of the website.
        nps_data_to_display["id"] = nps_id_attribute
        nps_data_to_display["fullName"] = nps_name_attribute
        nps_data_to_display["description"] = nps_description_attribute
        nps_data_to_display["latitude"] = nps_latitude_attribute
        nps_data_to_display["longitude"] = nps_longitude_attribute
        nps_data_to_display["states"] = nps_states_attribute
        nps_data_to_display["directionsUrl"] = nps_directions_attribute
        nps_data_to_display["image"] = nps_image_attribute
        
        # Add the state name, for use in the frontend, to
        # every dictionary in order to perform checks. --> MAYBE DELETE LATER!!!
        state_name = request.POST["state"].strip()
        nps_data_to_display["state_name"] = state_name
            
        # Also add the state abbreviation, called
        # state-code, for use in the frontend. 
        state_code = request.POST["state-code"].strip()
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
   Create the specific park for the web application.
"""
def specific_park(request):
    return render(request, 'Parks/pages/specific_park.html')
