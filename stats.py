def get_num_words(content):
    return len(content.split())

def get_num_chars(content):
    words_list = content.split()
    chars_dict = {}

    for word in words_list:
        for char in list(word):
            if char.lower() not in chars_dict:
                chars_dict[char.lower()] = 1
            else:
                chars_dict[char.lower()] += 1

    return chars_dict

def sort_on(dist):
    return dist["num"]

def sort_chars_dist(chars_dict):
    sorted_list = []

    for char, count in chars_dict.items():
        sorted_list.append({'char': char, 'num': count})
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list
