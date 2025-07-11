def get_num_words(text):
    words = text.split()
    sum = 0
    for word in words:
        sum+=1
    return sum

def get_letters_count(text):
    words = text.split()
    letters = []
    stats = {}

    for word in words:
        for letter in word:
            letters.append(letter.lower())

    for char in letters:
        if char not in stats:
            stats[char] = 1
        else:
            stats[char] += 1

    return stats

def sort_on(items):
    return items["num"]


def count_sort(dict):
    final_list = []
    for char in dict:
        char_stats = {}
        char_stats["char"] = char
        char_stats["num"] = dict[char]
        final_list.append(char_stats)

    final_list.sort(key=sort_on, reverse=True)
    return final_list

