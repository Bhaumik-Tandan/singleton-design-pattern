"""
Logger Singleton: Create a Logger class using the Singleton pattern. 
It should maintain a single instance throughout the program and allow multiple parts of the program to log messages.
"""

class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.log_messages = []
        return cls._instance

    def log(self, message):
        self.log_messages.append(message)

service1 = Logger()
service2 = Logger()

print(id(service1) == id(service2))  # Should print True

service1.log("Message from Service 1")
service2.log("Message from Service 2")

print(service1.log_messages)  
print(service2.log_messages)  
