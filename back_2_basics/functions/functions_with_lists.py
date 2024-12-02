#8-9
#Functions have been moved to messages_functions.py module, which we import below:
import messages_functions

#Importing specific functions from module
from messages_functions import display_messages, send_messages
#Importing all from module (not recommended)
from messages_functions import *
#Importing function name as alias from module (See line 25)
from messages_functions import send_messages as sm
#Importing module as alias to clean up code (See line 35)
import messages_functions as mf 

short_messages = ['Hello Jimmy.', 'Hope you have had a good day.', "I'll see you later!"]

#Using full module and function name
messages_functions.display_messages(short_messages)

#8-10
short_messages = ['Hello Jimmy.', 'Hope you have had a good day.', "I'll see you later!"]
sent_messages = []

#Call function, checks that the lists move their values properly
#Using alias name of function imported from module
sm(short_messages, sent_messages)
print(short_messages)
print(sent_messages)

#8-11
short_messages = ['Hello Jimmy.', 'Hope you have had a good day.', "I'll see you later!"]
sent_messages = []

#Pass a COPY of the list, so original list remains unchanged
#Using alias name for module
mf.send_messages(short_messages[:], sent_messages)
print(short_messages)
print(sent_messages)
