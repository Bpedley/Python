class Restaurant():
    
    """A class representing a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        print('Restaurant name: ' + self.restaurant_name + '\nCuisine type: ' + self.cuisine_type)

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        print(self.restaurant_name + ' is open. Welcome!')

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, add_number_served):
        """Allow user to increment the number of customers served."""
        self.number_served += add_number_served