from admin import Admin

egor = Admin('Dan', 'Nolan', 'Dann', 'Dann_@gmail.com', 'Paris')
egor.describe_user()
egor.privileges.privileges = ['can add post', 'can delete post', 'can ban user']
egor.privileges.show_privileges()