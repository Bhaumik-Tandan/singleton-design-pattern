"""
User Authentication: Implement a UserAuthenticator class using Singleton that handles user authentication. 
It should store user credentials and provide methods to validate user login attempts.
"""

class UserAuthenticator:
    _instance = None


    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.users = {}
        return cls._instance
    
    def add_user(self, username, password):
        self.users[username] = password
    
    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            return True
        return False

authenticator1 = UserAuthenticator()

authenticator1.add_user("user1", "password1")

authenticator2 = UserAuthenticator()

print(id(authenticator1) == id(authenticator2))  # Should print True


print(authenticator2.login("user1", "password1"))  # Should print True


print(authenticator2.login("user1", "password2"))  # Should print False


authenticator2.add_user("user2", "password2")

print(authenticator1.login("user2", "password2"))  # Should print True


print(authenticator1.login("user2", "password1"))  # Should print False


print(authenticator1.login("user1", "password1"))  # Should print True

