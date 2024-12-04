# Declaring the "name" variable, sending input from user.
name = input('Please enter your full name: ')

print() #blank line

# Printing static text, followed by "name" variable. Calling the title() method to auto-capitalize the name.
# Swapping between single and double quotes. Just stay consistent!
print('Hello', name.title(), '\nHave a "good" day.') # \n to make a new line.

#lower method converts strings to lowercase.
print('Here is your name in lowercase:', name.lower())

first_name = "glajummy"
last_name = "blain"

#f-strings: Format strings. Replace the name of bracketed variable with its value.
full_name = f"{first_name} {last_name}"

#Storing an f-string in a separate variable.
hello_message = f"Goodbye {full_name.title()}!\n\tHave a good day" #new line, tab out

print("Hello", full_name.title())
print(hello_message)