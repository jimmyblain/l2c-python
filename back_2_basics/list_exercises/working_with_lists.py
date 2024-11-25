#Looping through every item in a list

siblings = ['talisha', 'anthony', 'julie', 'davaunte', 'christina']
for sibling in siblings:
    print(f"{sibling.title()} is one of my siblings")
    print(f"I miss {sibling.title()} very much\n")
print("I will visit them soon.\n") #Indentation determines relation in code blocks

for value in range(1, 5): #range() method stops when it reaches the second number (off-by-one)
    print(value)