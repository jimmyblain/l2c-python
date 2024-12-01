#7-8, 9

#Define list of orders and empty list to move orders to.
sandwich_orders = ['cheeseburger', 'pastrami', 'chopped cheese', 'pastrami', 'bacon egg & cheese', 'philly cheesesteak', 'pastrami']
completed_orders = []


print("We apologize, but we have run out of pastrami! \n")

#Run while values exist in sandwich_orders
while sandwich_orders:

    #Remove all pastrami orders
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')

    #Pop value at the end of list, store in finished
    finished = sandwich_orders.pop()
    
    print(f"I made your {finished.title()} sandwich. ")

    #Append value in finished to list
    completed_orders.append(finished)

print(completed_orders)

#7-10

#Setting flag and defining empty dictionary
polling_active = True
responses = {}

while polling_active:
    
    name = input("\nWhat is your name? ")
    location = input("What is your dream job? ")

    responses[name] = location
    
    repeat = input("\n Is anyone else taking the poll? y/n ")
    if repeat == 'n':
        polling_active = False

#Polling complete
print("\n--- POLL RESULTS ---")
for name, location in responses.items():
    print(f"{name.title()} would like to be a {location.title()}.")
