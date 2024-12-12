#10-1, 3
from pathlib import Path

#Need to use relative path starting at project folder.
file_path = Path('back_2_basics/008_files_and_exceptions/learning_python.txt')

# Method chaining - runs methods from left to right
# This will strip the empty character/line at the end of the txt file
contents = file_path.read_text().rstrip()
print(f"{contents}\n")

# splitlines() returns a list of strings, line by line
for line in contents.splitlines():
    print(line)

# 10 -2
# replace() returns the line with the replaced text
message = ''
for old_line in contents.splitlines():
    message = old_line.replace('Python', 'C++')
    print(message)