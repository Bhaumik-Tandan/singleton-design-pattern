""" 
Resource Manager: Design a ResourceManager class using Singleton to manage shared resources 
(like files, sockets, etc.) across different parts of the program. 
Ensure that the resources are properly managed and accessed.
"""

class ResourceManager:
    _instance=None

    def __new__(cls):
        if cls._instance is None:
            cls._instance=super().__new__(cls)
            cls._instance.resources=[]
        return cls._instance

    def add_resource(self,resource):
        self.resources.append(resource)

    def get_resource(self):
        return self.resources.pop()

    def __str__(self):
        return str(self.resources)

manager1=ResourceManager()
manager2=ResourceManager()

print(id(manager1)==id(manager2))

manager1.add_resource("resource1")

print(manager2.get_resource())

manager2.add_resource("resource2")

print(manager1.get_resource())

manager1.add_resource("resource3")


print(manager1)
print(manager2)