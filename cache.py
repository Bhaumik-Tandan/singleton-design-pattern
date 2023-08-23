"""
Caching System: Implement a CacheManager class using Singleton that acts as a caching system for frequently accessed data. 
The class should allow data to be stored, retrieved, and invalidated.
"""

class CacheManager:
    _instance=None

    def __new__(cls):
        if cls._instance is None:
            cls._instance=super().__new__(cls)
            cls._instance.cache={}
        return cls._instance

    def store(self,key,value):
        self.cache[key]=value

    def retrieve(self,key):
        if key not in self.cache:
            return None
        return self.cache[key]

    def invalidate(self,key):
        del self.cache[key]

cache1=CacheManager()
cache2=CacheManager()

print(id(cache1)==id(cache2))

cache1.store("key1","value1")
cache1.store("key2","value2")

print(cache2.retrieve("key1"))
print(cache2.retrieve("key2"))

cache2.invalidate("key1")

print(cache1.retrieve("key1"))
print(cache1.retrieve("key2"))

cache1.invalidate("key2")

print(cache2.retrieve("key1"))

cache2.store("key3","value3")

print(cache1.retrieve("key3"))

cache1.invalidate("key3")

print(cache2.retrieve("key3"))


