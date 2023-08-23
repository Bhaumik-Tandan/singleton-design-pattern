class Counter:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.count = 0  # Initialize count only once
        return cls._instance

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def get_count(self):
        return self.count

counter1 = Counter()
counter2 = Counter()

print(id(counter1) == id(counter2))  # Should print True

counter1.increment()
counter1.increment()
counter2.decrement()
print(counter1.get_count())  # Should print 1
print(counter2.get_count())  # Should print 1

counter1.decrement()

print(counter1.get_count())  # Should print 0

print(counter1.get_count() == counter2.get_count())  # Should print True

counter2.increment()

print(counter1.get_count() == counter2.get_count())  # Should print True
