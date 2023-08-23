"""
Database Connection Pool: Design a DatabaseConnection class using Singleton to manage a pool of database connections.
 Ensure that the class maintains only one instance and provides a way to acquire and release connections.
"""

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connections = []  # Initialize connections only once
        return cls._instance

    def acquire_connection(self):
        if len(self.connections) > 0:
            return self.connections.pop(0)
        return None

    def release_connection(self, connection):
        self.connections.append(connection)

db_connection1 = DatabaseConnection()
db_connection2 = DatabaseConnection()

print(id(db_connection1) == id(db_connection2))  # Should print True

db_connection1.release_connection("Connection1")
db_connection1.release_connection("Connection2")

print(db_connection2.acquire_connection())  # Should print Connection1
print(db_connection2.acquire_connection())  # Should print Connection2
print(db_connection2.acquire_connection())  # Should print None
