def get_num_words(book):
    num_words = 0

    words = book.split()
    num_words = len(words)

    return num_words


def get_num_char(book):
    letter_dict = {}

    for char in book:
        if char.lower() not in letter_dict:
            letter_dict[char.lower()] = 1
        else:
            letter_dict[char.lower()] += 1

    return letter_dict 

def sort_on(dict_input):
    return dict_input["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list   
