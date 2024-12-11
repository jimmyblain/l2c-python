#10-1

from pathlib import Path

file_path = Path('learning_python.txt')
contents = file_path.read_text()
print(contents)