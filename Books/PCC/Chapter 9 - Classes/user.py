class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print(self.first_name + ' ' + self.last_name + '\nUsername: ' + self.username + '\nEmail: ' + \
        self.email + '\nLocation: ' + self.location)
    
    def greet_user(self):
        """Display a personalized greeting to the user."""
        print('Hello, ' + self.username + '!')

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0
