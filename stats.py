# stats.py

def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    text = text.lower()
    chars = {}
    for ch in text:
        if ch.isalpha():
            if ch in chars:
                chars[ch] += 1
            else:
                chars[ch] = 1
    return chars


def sort_characters(char_dict):
    char_list = []
    for ch, num in char_dict.items():
        char_list.append({"char": ch, "num": num})

    def sort_key(item):
        return item["num"]

    char_list.sort(reverse=True, key=sort_key)
    return char_list

