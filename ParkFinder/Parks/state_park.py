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
    
    def __init__(self, full_name, description, latitude, longitude, states, directionsUrl, image):
        
        self.full_name = full_name
        self.description = description
        self.latitude = latitude
        self.longitude = longitude
        self.states = states
        self.directionsUrl = directionsUrl
        self.image = image
        
    # def 
    
    # state name: kkkkkk state parks: {kkkkkkk}
        
        
        
    # REFERENCE THIS FOR THE IMAGE
    # nps_images_list = nps_first_element['images']
    # nps_image_element = nps_images_list[0]
    # nps_image_attribute = nps_image_element['url']