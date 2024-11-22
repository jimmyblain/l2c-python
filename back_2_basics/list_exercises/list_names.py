#Square brackets [] signify a list (similar to an Array)

family = ['talisha', 'anthony', 'julie', 'davaunte', 'christina']


print(family) #Printing a List without specifying an element will print the entire list
print(family[0].title()) #You can call methods on specific List elements
print(family[-1].title()) #Best way to reference last element in a List

print("My youngest sibling is", family[3].title())
print("My oldest sibling is", family[2].title())

#Append item to the end of a List
family.append('jaime')
print(family)

colors = [] #define an empty list
colors.append('red')
colors.append('white')
colors.append('blue')
print(colors)

#Inserting an element into a List
colors.insert(2, 'green')
print(colors)

#Removing elements from a List based on Index
del colors[2]
print(colors)

#Removing and storing an element in a List
popped_sister = family.pop() #Enter index value within () to specify an element, otherwise pops from end of List
print(family)
print(f"The sister we don't talk to is {popped_sister.title()}.")

#Removing an elements from a List based on Value. Note: Only removes FIRST instance of the value, loop through List to remove all
colors.remove('white')
print(colors)

#Sorting a list temporarily
print(family)
print(sorted(family))

#Reversing the order of a list (permanent, run a again to revert)
family.reverse()
print(family)

#Sort alphabetically (permanent, cannot revert)
family.sort()
print(f"My sibilings in alphabetical order are {family}")
family.sort(reverse=True)
print(f"My siblings is reverse-alphabetical order are {family}")

#Finding the length of a list
print(f"I have {len(family)} siblings")