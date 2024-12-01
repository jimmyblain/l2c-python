#8-9

short_messages = ['Hello Jimmy.', 'Hope you have had a good day.', "I'll see you later!"]

def display_messages(messages):
    """Pass a list of messages, print each message in the list"""
    while messages:
        current_message = messages.pop()
        print(current_message)

display_messages(short_messages)

#8-10
short_messages = ['Hello Jimmy.', 'Hope you have had a good day.', "I'll see you later!"]
sent_messages = []

def send_messages(message_queue, messages_sent):
    """Pass a list of messages, and an empty list. As messages are sent, move them to the empty list"""
    while message_queue:
        current_message = message_queue.pop()
        print(current_message)
        messages_sent.append(current_message)

#Call function, checks that the lists move their values properly
send_messages(short_messages, sent_messages)
print(short_messages)
print(sent_messages)

#8-11
short_messages = ['Hello Jimmy.', 'Hope you have had a good day.', "I'll see you later!"]
sent_messages = []

#Pass a COPY of the list, so original list remains unchanged
send_messages(short_messages[:], sent_messages)
print(short_messages)
print(sent_messages)
