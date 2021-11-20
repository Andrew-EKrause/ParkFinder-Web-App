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
    
    # Here we use the National Park Services (NPS) API to obtain all of
    # the parks a selected state. WE MAY WANT TO ADD THIS OUTSIDE OF VIEWS
    # SO WE DO NOT EXCEED OUR LIMIT OF 1,000 REQUESTS PER HOUR TO THE NPS API.
    
    # -------------------------------------------------------------------------

    # --> Configure API request - GET THIS DONE!!!

    # First use the installed django extension for the api, called natlparks.
    parks = NatlParks("XApMBEDd2SIXa1aX7bakVem1E28W0wWgtHuGn3SF")
    
    # STEP 1 (API): Create a list variable to store the data 
    # returned from the api request.
    nps_data_to_parse = []
    nps_data_to_parse = parks.parks(limit=1, start=1)
    nps_data_dict = {}
    nps_data_dict = nps_data_to_parse['data']
    nps_first_element = nps_data_dict[0]
    
    # STEP 2 (API): Obtain specific data attributes from the data dictionary.
    nps_name_attribute = nps_first_element['fullName']
    nps_description_attribute = nps_first_element['description']
    nps_latitude_attribute = nps_first_element['latitude']
    nps_longitude_attribute = nps_first_element['longitude']
    nps_states_attribute = nps_first_element['states']
    nps_directions_attribute = nps_first_element['directionsUrl']
    
    nps_images_list = nps_first_element['images']
    nps_image_element = nps_images_list[0]
    nps_image_attribute = nps_image_element['url']

    # --> DEBUGGING PRINT STATEMENTS
    # print(nps_name_attribute)
    # print(nps_description_attribute)
    # print(nps_latitude_attribute)
    # print(nps_longitude_attribute)
    # print(nps_states_attribute)
    # print(nps_directions_attribute)
    # print(nps_image_attribute)
    
    # STEP 3 (API): Place the obtained data in a dictionariy that 
    # will be passed to the frontend of the web application.
    nps_data_to_display = {}
    nps_data_to_display["fullName"] = nps_name_attribute
    nps_data_to_display["description"] = nps_description_attribute
    nps_data_to_display["latitude"] = nps_latitude_attribute
    nps_data_to_display["longitude"] = nps_longitude_attribute
    nps_data_to_display["states"] = nps_states_attribute
    nps_data_to_display["directionsUrl"] = nps_directions_attribute
    nps_data_to_display["image"] = nps_image_attribute

    # -------------------------------------------------------------------------

    # STEP 4 (OTHER): Add a key value pair to the nps data dictionary, 
    # which is the name of the state.  
    state_name = request.POST['state'].strip()
    nps_data_to_display["state_name"] = state_name
    
    # Also add the state abbreviation, called
    # state-code, for use in the frontend. 
    state_code = request.POST['state-code'].strip()
    nps_data_to_display["state_code"] = state_code

    # If the method is a post requst, render the data for the park on 
    # screen. Otherwise, redirect to the find parks page of the website.
    if request.method == "POST":
        return render(request, 'Parks/pages/parks.html', nps_data_to_display)
    else:
        return redirect("ParkFinder-find_parks")

"""
   Create the specific park for the web application.
"""
def specific_park(request):
    return render(request, 'Parks/pages/specific_park.html')


#######################################################################


# """
#     Author: Riley Radle
#     Description:
#     Views.py is responsible for routing to and from the html pages.
#     It handles requests from the user, querying the database, and more.
#     This is the main backend file which handles the information about the store.
# """

# from django.shortcuts import render
# from .models import Item, Category
# from .utils import utils


# """
#     NOTE: 
#     @param 'request' is a string representation 
#     of the request that is generated from the html pages.
#     Each view get's their own request object.
# """

# """
#     Render the home html page to the browser.
# """
# def home(request):
#     # DO NOT UNCOMMENT, used to quickly/automatically add items to database.
#     # utils.add_database_categories()
#     # utils.add_database_items()
#     return render(request, "Store/pages/home.html")


# """
#     Render the login html page to the browser.
# """ 
# def login(request):
#     return render(request, "Store/pages/login.html")


# """
#     Display all of the items that have the given category.
#     @param name: The name of the category from which to get and display items. 
# """ 
# def view_category(request, name):
#     # Get the items associated with the category for displaying
#     data_to_display = {
#         "category_items" : utils.get_category_items(name)
#     }

#     return render(request, "Store/pages/view_category.html", data_to_display)


# """
#     Display the items that match the user's search. 
# """
# def search_results(request): 

#     # The user searched for an item.
#     if request.method == "POST":
#         data_to_display = {}

#         # Strip the whitespace off of the user's search and make it lowercase
#         # Then get the search results
#         search_string = request.POST['searched_string'].strip().lower()
#         search_results = utils.get_search_results(search_string)

#         # Record the data for displaying
#         data_to_display["search_string"] = search_string
#         data_to_display["search_results"] = search_results

#         return render(request, "Store/pages/search_results.html", data_to_display)

#     # The user did not search for an item.
#     return render(request, "Store/pages/search_results.html")


# """
#     Display a single item and all of it's relevant information. 
#     @param name: The name of the item to display.
# """
# def view_item(request, name):

#     # Query the database for the current item.
#     current_item = Item.objects.get(pk=name)
#     data_to_display = {
#         "current_item" : current_item
#     }

#     # The user tried to add or remove an item from cart
#     if request.method == "POST":

#         # If the item was in the cart, the user is removing it
#         if current_item.in_cart:
#             utils.remove_from_cart(current_item)

#         # Else they must have been adding the item
#         else:
#             utils.add_to_cart(current_item)
         
#     return render(request, "Store/pages/view_item.html", data_to_display)


# """
#     Display the items in the current user's cart.
#     @param name: The name of an item to remove from cart (if the user wishes to do so) 
# """
# def view_cart(request, name=None):

#     # User wants to remove an item from the cart
#     if request.method == "POST":
#         item = Item.objects.get(pk=name)
#         utils.remove_from_cart(item)

#     # Get the cart items and determine the total
#     cart = utils.get_cart_items()
#     total = utils.sum_prices(cart)

#     # Dictionary of data to display in the html
#     data_to_display = {
#         "cart" : cart,
#         "total" : "%.2f"%total
#     }

#     return render(request, "Store/pages/view_cart.html", data_to_display)


# """
#     Display the items in the user's cart for checking out. 
# """
# def checkout(request):
#     # Get the cart items and determine the total
#     cart = utils.get_cart_items()
#     total = utils.sum_prices(cart)

#     # Determine the subtotal
#     subtotal = total + (total * utils.tax_rate) + utils.shipping
#     tax = total * utils.tax_rate 

#     # Dictionary of data to display in the html
#     data_to_display = {
#         "cart" : cart,
#         "total" : "%.2f"%total, 
#         "subtotal" : "%.2f"%subtotal,
#         "tax" : "%.2f"%tax,
#         "shipping" : "%.2f"%utils.shipping 
#     }    

#     return render(request, "Store/pages/checkout.html", data_to_display)

# """
#     Display the items that match the user's search. 
# """
# def search_results(request): 

#     # The user searched for an item.
#     if request.method == "POST":
#         data_to_display = {}

#         # Strip the whitespace off of the user's search and make it lowercase
#         # Then get the search results
#         search_string = request.POST['searched_string'].strip().lower()
#         search_results = utils.get_search_results(search_string)

#         # Record the data for displaying
#         data_to_display["search_string"] = search_string
#         data_to_display["search_results"] = search_results

#         return render(request, "Store/pages/search_results.html", data_to_display)

#     # The user did not search for an item.
#     return render(request, "Store/pages/search_results.html")
