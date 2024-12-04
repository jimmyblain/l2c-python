#8-15
#Moved these functions from functions_with_lists.py, see that file for comments
#This is now a module that will be imported by that program


def display_messages(messages):
    """Pass a list of messages, print each message in the list"""
    while messages:
        current_message = messages.pop()
        print(current_message)


def send_messages(message_queue, messages_sent):
    """Pass a list of messages, and an empty list. As messages are sent, move them to the empty list"""
    while message_queue:
        current_message = message_queue.pop()
        print(current_message)
        messages_sent.append(current_message)