# 10-8, 9
from pathlib import Path

def print_list(lines):
    '''Print the list line by line'''
    for line in lines.splitlines():
        print(line)

# Store contents of text files in variables
cat_path = Path('back_2_basics/008_files_and_exceptions/cats.txt')
dog_path = Path('back_2_basics/008_files_and_exceptions/dogs.txt')

# Try to read cats.txt
# If it doesn't exist, throw error. If it does, print line by line
try:
    cat_contents = cat_path.read_text()
except FileNotFoundError:
    print(f"The file '{cat_path}' does not exist")
else:
    print_list(cat_contents)

# Try to read dogs.txt
# If it doesn't exist, do nothing. If it does, print line by line
try:
    dog_content = dog_path.read_text()
except FileNotFoundError:
    pass
    #print(f"The file '{dog_path}' does not exist.")
else:
    print_list(dog_content)