# Configuration Manager: Implement a Configuration class using Singleton to manage application configurations. 
# It should ensure that only one instance of the Configuration class exists and provide methods to read and update configuration values.

class Configuration:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.config = {}
        return cls._instance

    def get_config(self, key):
        return self.config.get(key)

    def set_config(self, key, value):
        self.config[key] = value

config_manager1 = Configuration()
config_manager2 = Configuration()


print(id(config_manager1) == id(config_manager2))  # Should print True

config_manager1.set_config("version", "1.0")
config_manager2.set_config("version", "2.0")

print(config_manager1.get_config("version"))  # Should print 2.0
print(config_manager2.get_config("version"))  # Should print 2.0
