"""
Global Event Dispatcher: Design a GlobalEventDispatcher class using Singleton that can be used to subscribe and dispatch global events within the application.
 Different parts of the program should be able to listen for and emit events.
"""


class GlobalEventDispatcher:
    _instance=None

    def __new__(cls):
        if cls._instance is None:
            cls._instance=super().__new__(cls)
            cls._instance.listeners={}
        return cls._instance

    def subscribe(self,event,listener):
        if event not in self.listeners:
            self.listeners[event]=[]
        self.listeners[event].append(listener)

    def unsubscribe(self,event,listener):
        if event not in self.listeners:
            return
        self.listeners[event].remove(listener)

    def dispatch(self,event,data=None):
        if event not in self.listeners:
            return
        for listener in self.listeners[event]:
            listener(data)

dispatcher1=GlobalEventDispatcher()
dispatcher2=GlobalEventDispatcher()

print(id(dispatcher1)==id(dispatcher2))

def listener1(data):
    print("Listener 1 received data: "+str(data))

def listener2(data):
    print("Listener 2 received data: "+str(data))

dispatcher1.subscribe("event1",listener1)

dispatcher2.subscribe("event1",listener2)

dispatcher1.dispatch("event1","abc")
dispatcher2.dispatch("event1","def")

dispatcher1.unsubscribe("event1",listener1)

dispatcher1.dispatch("event1","ghi")
dispatcher2.dispatch("event1","jkl")

dispatcher2.unsubscribe("event1",listener2)

dispatcher1.dispatch("event1","mno")

dispatcher1.subscribe("event2",listener1)

dispatcher1.dispatch("event2","pqr")
dispatcher2.dispatch("event2","stu")

dispatcher1.unsubscribe("event2",listener1)

dispatcher1.dispatch("event2","vwx")

dispatcher2.subscribe("event2",listener2)

dispatcher1.dispatch("event2","yz")

dispatcher2.unsubscribe("event2",listener2)

dispatcher2.dispatch("event2","123")

dispatcher1.subscribe("event3",listener1)

dispatcher1.dispatch("event3","456")

dispatcher1.unsubscribe("event3",listener1)

dispatcher1.dispatch("event3","789")

dispatcher2.subscribe("event3",listener2)

dispatcher2.dispatch("event3","0ab")

dispatcher2.unsubscribe("event3",listener2)

dispatcher2.dispatch("event3","cde")
