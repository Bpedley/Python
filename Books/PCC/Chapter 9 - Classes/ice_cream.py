from restaurant import Restaurant

class IceCreamStand(Restaurant):
    """Represent an ice cream stand."""
    
    def __init__(self, restaurant_name, cuisine_type='ice_cream'):
        """Initialize an ice cream stand."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def print_flavors(self):
        """Display the flavors available."""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print('- ' + flavor.title())