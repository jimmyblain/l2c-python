#6-1, 2, 3, 4

#Defining a dictionary with key-value pairs.
alicia = {'gender' : 'female', 'age' : 36, 'race' : 'black'}
print(alicia['gender'].title())
print(alicia['age'])
print(alicia['race'].upper())

#Defining a dictionary of similar objects with one piece of information
fav_numbers = {
    'jimmy' : 777,
    'alicia' : 27,
    'anthony' : 324720,
    'talisha' : 1,
    'stina' : 777,
    "tae" : 27,
}

print(f"Jimmy's favorite number is {fav_numbers['jimmy']}")

#Use get() method to retrieve data from a list, and provide a default if no data is detected.
ant_fav_number = fav_numbers.get('anthony', 'No favorite number specified.')
print(f"Anthony's favorite number is {ant_fav_number}")

glossary = {
    'list' : 'a collection of data of similar type',
    'for loop' : 'a block of code that repeats depending on a stated condition',
    'if statement' : 'a block of code that executes once if a condition is met',
    'else statement' : 'a block of code that executes when the if statement condition(s) fail',
    'dictionary' : 'a collection of key-value pairs, meant to connect related data',
    'variable' : 'defined, named data meant to represent a value in an understandble and readable way',
    'tuple' : 'a list in which the indexed values do not change',
    'set' : 'a collection in which each item much be unique',
}

#Looping through key-value pairs in a dictionary.
#Define two variables to hold the values, and call the items() method.
for words, definitions in glossary.items():
    print(f"The definition of a {words.title()} is: {definitions}.\n")

#Looping through just the keys in alphabetical order using sorted() method.
#Looping through keys is the default behavior; you don't need to explicitly call the keys() method.
for words in sorted(glossary.keys()):
    print(f"The words we are defining are: {words.title()}")

#6-5
print("Flashcard excercise! Can you identify the corresponding python concept with its definition below:")
for definitions in glossary.values():
    print(f"\t - {definitions}")

#6-6
participants = ['alicia', 'glaj', 'jimmy', 'anthony', 'alain']

for people in participants:

    if people in fav_numbers.keys():
        print(f"Thanks for sharing your favorite number {people.title()}")
    else:
        print(f"You haven't given us your favorite number yet, {people.title()}")