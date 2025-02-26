def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_character_counts(char_dict):
    char_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            char_list.append({char: count})
    char_list.sort(reverse=True, key=lambda x: list(x.values())[0])
    return char_list

