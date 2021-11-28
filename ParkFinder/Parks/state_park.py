#
# CS 224 Fall 2021
# Semester Project
#
# The state park class helps to organize the park data
# that is transmitted by the API. The park data is 
# organized into lists of information that can be 
# accessed in a more easy manner as opposed to 
# traversing through the API dictionary representation
# of the data.
#
# Author: Andrew Krause
# Date: TBD
#
class state_park():
    
    # Create an initialization function (similar to a constructor) in order to
    # create a new state_park() object when needed. This will be added to a list.
    def __init__(self, full_name, description, latitude, longitude, states, directions_url, image):
        
        self.full_name = full_name
        self.description = description
        self.latitude = latitude
        self.longitude = longitude
        self.states = states
        self.directions_url = directions_url
        self.image = image
    
    # Create GETTERS for the state_park() class.
    def get_name(self):
        return self.full_name;
    
    def get_description(self):
        return self.description;
    
    def get_latitude(self):
        return self.latitude;
    
    def get_longitude(self):
        return self.longitude;
    
    def get_states(self):
        return self.states;
    
    def get_directions(self):
        return self.directionsUrl;
    
    def get_image(self):
        return self.image;
    
    # Create SETTERS for the state_park() class.
    def set_name(self, new_name):
        self.full_name = new_name;
    
    def set_description(self, new_description):
        self.description = new_description;
    
    def set_latitude(self, new_latitude):
        self.latitude = new_latitude;
    
    def set_longitude(self, new_longitude):
        self.longitude = new_longitude;
    
    def set_states(self, new_states):
        self.states = new_states;
    
    def set_directions(self, new_directions_url):
        self.directions_url = new_directions_url;
    
    def set_image(self, new_image):
        self.image = new_image;
        
        
        
    # REFERENCE THIS FOR THE IMAGE
    # nps_images_list = nps_first_element['images']
    # nps_image_element = nps_images_list[0]
    # nps_image_attribute = nps_image_element['url']