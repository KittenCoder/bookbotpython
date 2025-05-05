import os.path
import sys
from stats import get_words_in_text, get_char_counts

def get_book_text(filepath):
    contents = ""
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    # Config
    book_path = sys.argv[1]

    # Print
    print(f"Analyzing book found at {book_path}...")
    # Get content
    book_contents = get_book_text(book_path)
    # Print
    print("----------- Word Count -------")
    # Get word count
    word_count = get_words_in_text(book_contents)
    # Print
    print(f'Found {word_count} total words')
    print("----------- Character Count -----------")
    # Get character counts
    char_counts = get_char_counts(book_contents)
    char_counts_string = ""
    char_counts_keys = char_counts.keys()
    for key in char_counts_keys:
        if not key.isalpha():
            continue
        char_counts_string += key + ": " + str(char_counts[key]) + f'\n'
    # Print
    print(char_counts_string, end="")

if __name__ == '__main__':
    if not len(sys.argv) == 2:
        print(f'Usage: python3 {sys.argv[0]} <path_to_book>')
        sys.exit(1)
    if not os.path.isfile(sys.argv[1]):
        print("Error: File does not exist")
        sys.exit(1)
    print("============ BOOKBOT ============")
    main()
    print("============ END ============")
