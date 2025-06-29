def get_num_words(text):
    return len(text.split())

def get_char_count(text):
    chars = {}
    for char in text:
        c = char.lower()
        if c not in chars:
            chars[c] = 1
        else:
            chars[c] += 1
    return chars

def sort_on(items):
    return items["num"]

def sort_dict(dict):
    dict_list = []
    for key in dict:
        dict_list.append({"char": key, "num": dict[key]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list