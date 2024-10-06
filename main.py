def main():
    book_url = get_user_book_input()
    book_text = get_book_text(book_url)
    total_book_words = count_book_words(book_text)
    chars_appearances = characters_dictionary(book_text)
    list_chars_appearances = create_list_of_dicts(chars_appearances)
    print(f"--- Begin report of {book_url} ---")
    print(f"{total_book_words} words found in document.")
    print("\n")
    display_all_occurences(list_chars_appearances)
    print('--- End report ---')
    

def get_book_text(path):
    try:
        with open(path) as book:
            book_content = book.read()
            return book_content
    except FileNotFoundError:
        print(f"The {path} was not found. Please try again!")
    except Exception as error:
        print(error)

def count_book_words(book_text):
    words_list = book_text.split()
    words_total = len(words_list)
    return words_total

def characters_dictionary(book_text):
    chars_dict = {}
    for char in book_text:
        lowercase_char = char.lower()
        if lowercase_char in chars_dict:
            chars_dict[lowercase_char] += 1
        else:
            chars_dict[lowercase_char] = 1
    return chars_dict


def create_list_of_dicts(dict):
    dicts_list = []
    for letter in dict:
        if letter.isalpha():
            current_new_dict={}
            current_new_dict['letter'] = letter
            current_new_dict['number'] = dict[letter]
            dicts_list.append(current_new_dict)
    return dicts_list


def sort_after(dict):
    return dict['number']

def display_all_occurences(list):
    list.sort(reverse=True, key=sort_after)
    for dict in list:
        print(f'The {dict['letter']} character was found {dict['number']} times')


def get_user_book_input():
    book_path = str(input('Please type in your .txt file path from your current folder:'))
    return book_path


main()