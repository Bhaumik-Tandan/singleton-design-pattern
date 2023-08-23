"""
System Health Monitor: Create a SystemHealthMonitor class using Singleton that monitors the health of various system components. 
It should provide methods to add, update, and retrieve health status information.
"""

class SystemHealthMonitor:
    _instance=None

    def __new__(cls):
        if cls._instance is None:
            cls._instance=super().__new__(cls)
            cls._instance.health={}
        return cls._instance

    def add(self,component,status):
        self.health[component]=status

    def update(self,component,status):
        self.health[component]=status

    def retrieve(self,component):
        if component not in self.health:
            return None
        return self.health[component]


monitor1=SystemHealthMonitor()
monitor2=SystemHealthMonitor()

print(id(monitor1)==id(monitor2))

monitor1.add("component1","status1")
monitor1.add("component2","status2")

print(monitor2.retrieve("component1"))
print(monitor2.retrieve("component2"))

monitor2.update("component1","status3")
monitor1.update("component2","status4")

print(monitor1.retrieve("component1"))
print(monitor1.retrieve("component2"))

monitor1.update("component1","status5")

print(monitor2.retrieve("component1"))

monitor2.add("component3","status6")

print(monitor1.retrieve("component3"))

monitor1.update("component3","status7")

print(monitor2.retrieve("component3"))

monitor2.add("component4","status8")