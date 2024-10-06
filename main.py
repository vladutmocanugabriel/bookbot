def main():
    book_url = "books/frankenstein.txt"
    book_text = get_book_text(book_url)
    total_book_words = count_book_words(book_text)
    print(f"The book has a total of {total_book_words} words.")  
    print(f"The book has the following chars count: {characters_dictionary(book_text)}")


def get_book_text(path):
    with open(path) as book:
        book_content = book.read()
        return book_content

def count_book_words(book_text):
    words_list = book_text.split()
    words_total = len(words_list)
    return words_total

def characters_dictionary(book_text):
    words_list = book_text.split()
    chars_list = []
    chars_dictionary = {}
    for word in words_list:
        for char in word:
            chars_list.append(char.lower())
    chars_set = set(chars_list)
    chars_list_no_duplicates = list(chars_set)
    
    for char in chars_list_no_duplicates:
        chars_dictionary[char] = 0
        for elem in chars_list:
            if char == elem:
                chars_dictionary[char] += 1
    return chars_dictionary
            
            


main()