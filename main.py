from sys import argv, exit
from stats import *

def main():
    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    path = argv[1]
    content = get_book_text(path)
    char_dist = get_num_chars(content)
    char_list = sort_chars_dist(char_dist)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(content)} total words")
    print("--------- Character Count -------")
    for char_dist in char_list:
        if char_dist["char"].isalpha():
            print(f"{char_dist['char']}: {char_dist['num']}")
    print("============= END ===============")

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

main()
