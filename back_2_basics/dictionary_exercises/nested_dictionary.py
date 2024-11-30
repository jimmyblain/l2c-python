#6-7, 8

#Defining multiple dictories with the same data formatting
user_0 = {
    'first_name' : 'glajummy',
    'last_name' : 'blain',
    'city' : 'atlanta',
}

user_1 = {
    'first_name' : 'talisha',
    'last_name' : 'blain',
    'city' : 'new york',
}

user_2 = {
    'first_name' : 'fenton',
    'last_name' : 'gardner',
    'city' : 'atlanta',
}

user_3 = {
    'first_name' : 'alicia',
    'last_name' : 'blain',
    'city' : 'atlanta',
}

#Nested dictionaries to a list
people = [user_0, user_1, user_2, user_3]

#Loop through list of dictionaries and print specific values 
for peeps in people:
    print(f"{peeps['first_name'].title()} {peeps['last_name'].title()} lives in {peeps['city'].title()}")

#6-9

#Nested lists in dictionary
favorite_places = {
    'jimmy' : ['san francisco', 'madrid', 'italy'],
    'alicia' : ['ghana', 'south africa'],
    'talisha' : ['mexico', 'jamaica', 'aruba'],
}

#Looping first through dictionary keys, then through the lists-values
for names, places in favorite_places.items():
    print(f"\n{names.title()}'s favorite places are: ")

    for place in places:
        print(f"\t{place.title()}")


#6-10

fav_numbers = {
    'jimmy' : [777, 498],
    'alicia' : [27, 9, 3],
    'anthony' : [324720, 42, 1],
    'talisha' : [1],
    'stina' : [777, 333],
    "tae" : [27, 2, 4],
}

for names, numbers in fav_numbers.items():
    if len(numbers) == 1:
        print(f"\n{names.title()}'s favorite number is: ")
    else:
        print(f"\n{names.title()}'s favorite numbers are: ")

    for number in numbers:
        print(f"\t{number}")

#6-11

#Nesting dictionary within a dictionary 
cities = {
    'new york' : {
        'country' : 'usa',
        'population' : 8000000,
        'fact' : "it's mad brick right now",
    },

    'madrid' : {
        'country' : 'spain',
        'population' : 1000000,
        'fact' : "it's a great vacation spot",
    },

    'london' : {
        'country' : 'uk',
        'population' : 5000000,
        'fact' : "there is a big clocktower here",
    }
}

for city, stats in cities.items():
    print(f"\nHere are some facts about {city.title()}:")
    for trait, factoid in stats.items():
        print(f"\t{trait.title()} is: {factoid}.")

