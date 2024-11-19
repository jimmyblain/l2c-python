#2-3, 2-4
person_name = "johnny Depp"
print(person_name)
print(person_name.upper())
print(person_name.lower())
print(person_name.title())

#2-5, 2-6
message = 'In the chacter of Jack Sparrow,', person_name.title(),', was the worst pirate you have ever heard of.\nBut as he said "you have heard of him!"'
print(message)

#2-7
new_name = "  Jimmy \n\t Blain    "
print("Hello", new_name, "you're cool")
print("Hello", new_name.rstrip(), "you're cool")
print("Hello", new_name.lstrip(), "you're cool")
print("Hello", new_name.strip(), "you're cool")

#2-8
with_extension = "SSN.txt"
print(with_extension)
without_extension = with_extension.strip(".txt")
print(without_extension)

#2-9, 2-10
print(6+2)
print(16/2)
print(2*4)
print(11-3)

favorite_number = 1337
CONSTANT_FAV = 777
print("My favorite number is", favorite_number)