import sys
from stats import *

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
        text = get_book_text(path)
    
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        print(f"Found {get_num_words(text)} total words")
        print("--------- Character Count -------")
        for dict in count_sort(get_letters_count(text)):
            if dict["char"].isalpha():
                print(f"{dict["char"]}: {dict["num"]}")
        print("============= END ===============")
    


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents





main()