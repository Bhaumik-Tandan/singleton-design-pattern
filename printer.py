"""
Print Spooler Singleton: Create a PrintSpooler class using Singleton that simulates a print spooler. 
It should allow multiple print requests to be queued and processed in the order they were received.
"""

class PrintSpooler:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.queue = []
        return cls._instance

    def add_print_request(self, print_job):
        self.queue.append(print_job)
        
    def process_print_requests(self):
        if len(self.queue) > 0:
            print(self.queue.pop(0))
        else:
            print("No more print jobs in queue")

spooler1 = PrintSpooler()
spooler2 = PrintSpooler()   

print(id(spooler1) == id(spooler2))  # Should print True

spooler1.add_print_request("Job 1")
spooler1.add_print_request("Job 2")

spooler2.process_print_requests()  # Should print Job 1
spooler1.process_print_requests()  # Should print Job 2

spooler1.process_print_requests()  # Should print No more print jobs in queue
spooler2.process_print_requests()  # Should print No more print jobs in queue

spooler2.add_print_request("Job 3")

spooler1.process_print_requests()  # Should print Job 3

spooler1.process_print_requests()  # Should print No more print jobs in queue

spooler2.process_print_requests()  # Should print No more print jobs in queue