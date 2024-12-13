# 10 6, 7

print("This program accepts two integers and adds them together.\n Enter q to quit.")

# Run these prompts continuously until user decides to quit
while True:
    first_number = (input("Enter the first number: "))
    if first_number == 'q':
        break
    second_number = (input("Enter the second number: "))
    if second_number == 'q':
        break
    
    # Only wrap try block around line that causes potential error
    try:
        sum = int(first_number) + int(second_number)
    # Use error name that appears in traceback    
    except ValueError:
        print("One or more of your inputs is not an integer.")
    else:
        print(f"The sum of your two numbers is: {sum}")