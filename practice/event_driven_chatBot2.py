from datetime import datetime
import time

class EventDrivenChatBot:
    
    def __init__(self):
        # accepted_messages maps incoming messages to 
        # list of callback functions
        self.accepted_messages = {}
        
        # time of instantiation
        self.birth_time = datetime.now()

        # create member varible
        self.has_been_asked_age = False;
        
        # "registering" all callbacks
        self.register_callback("hi", 
                               self.respond_to_greeting)
        self.register_callback("bye", 
                               self.respond_to_departure)

        # two callback function associatd with the same message
        self.register_callback("age?",
                               self.respond_to_age_request_detailed)
        self.register_callback("age?",
                               self.respond_to_age_request)

        # register handler
        self.register_callback("age?",
                                self.handle_age_request)
    
    def register_callback(self, message, callback): # callback is function_name
        """
        Registers a callback to a message.
        """
        if message not in self.accepted_messages:
            self.accepted_messages[message] = []
        self.accepted_messages[message].append(callback)
        
    def respond_to_greeting(self):
        print("Hello!")
        
    def respond_to_departure(self):
        print("Nice chatting with you!")
            
    def respond_to_age_request(self):
        age = datetime.now() - self.birth_time
        print("I am", age.seconds, "seconds old.")
        
    def respond_to_age_request_detailed(self):
        age = datetime.now() - self.birth_time
        micros = age.microseconds
        print("Technically, I'm", age.seconds, "seconds and", 
              micros, "microseconds old")
        
    def handle_message(self, message):
        if message not in self.accepted_messages:
            print("sorry, I don't understand", message)
        else:
            callbacks = self.accepted_messages[message] # find the name of corresponding callback function
            for callback in callbacks:
                callback() # execute callback function

    def handle_age_request(self, message):
        if not self.has_been_asked_age:
            self.has_been_asked_age = True
            self.respond_to_age_request()
        else:
            self.respond_to_age_request_detailed()


                
bot = EventDrivenChatBot()
bot.handle_message("hi")
time.sleep(2.2)
#bot.handle_message("age?")
bot.handle_age_request("age?")
bot.handle_message("bye")