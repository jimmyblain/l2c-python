# 10-10
from pathlib import Path

file_path = Path('back_2_basics/008_files_and_exceptions/prideandprejudice.txt')
book_words = file_path.read_text()

# Convert words to lower case, count how many times "the" appears
# Include the space after so you don't count words like "then" and "there"
the_count = book_words.lower().count('the ')
print(f"The word appears {the_count} times.")