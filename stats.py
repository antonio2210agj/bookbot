def number_of_words(text):
    words = text.split()
    return f"Found {len(words)} total words"

def character_appearances(text):
    my_dict = {}
    text = text.lower()
    for character in text:
        if character in my_dict:
            my_dict[character] += 1
        else:
            my_dict[character] = 1
    return my_dict

def sort_dict(char_dict):
    char_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})
    char_list.sort(reverse=True, key=lambda d: d["num"])
    return char_list
