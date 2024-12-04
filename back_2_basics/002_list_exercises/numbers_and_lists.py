#Testing for loops, range and statistical methods

#4-3
for number in range(1,21): #Iterated through n to n-1
    print(number)

#4-4
millions = []
for value in range(1, 1000001):
    millions.append(value)
#print (millions)
#Commented out to save code space ^

#4-5
print(min(millions))
print(max(millions))
print(sum(millions))

#4-6
odd_numbers = list(range(1,21,2))
for number in odd_numbers:
    print(number)

#4-7
threes = []
for value in range(3,31,3):
    threes.append(value)
print(threes)

#4-8
cubes = []
for value in range(1,11):
    cubes.append(value**3)
print(cubes)

#4-9
new_cube = [new_val**3 for new_val in range(1,11)]
print(new_cube)

#4-10
print(new_cube[:3]) #Slice: grab the first 3 elements
print(new_cube[3:6]) #Grab 3 elements, starting at index 3 through the 5th (6-1)
print(new_cube[-3:]) #Grab the last 3 elements

#4-11
siblings = ['talisha', 'anthony', 'julie', 'davaunte', 'christina']
alicia_stepsibs = siblings[:] #when making a copy of a list, use an empty Slice

siblings.append('jaime')
alicia_stepsibs.append('jackie')

print("\nMy siblings are: ")
for sibling in siblings:
    print(sibling.title())

print("\nMy wife's step siblings are: ")
for alicia_sibling in alicia_stepsibs:
    print(alicia_sibling.title())

#4-13
buffet = ('steak', 'chicken', 'tofu', 'pork', 'salmon') #Tuple: List with unchanging elements
for meat in buffet:
    print(meat)

#buffet[3] = 'lamb' - Commented out because you cannot change elements in a tuple
buffet = ('steak', 'chicken', 'lamb', 'veel', 'salmon') #Can redefine a tuple to change values
for meat in buffet:
    print(meat)
