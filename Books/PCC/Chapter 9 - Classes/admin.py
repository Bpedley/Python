from user import User

class Admin(User):
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the admin."""
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()


class Privileges():
    """Stores privileges associated with an Admin account."""

    def __init__(self, privileges=[]):
        """Initialize the privileges object."""
        self.privileges = privileges

    def show_privileges(self):
        """Display the privileges this administrator has."""
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print('- ' + privilege)
        else:
            print('- This user has no privileges.')