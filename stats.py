def get_word_count(text):
    words = text.split()
    count = len(words)
    return count


def get_character_count(text):
    lowered = text.lower()
    character_count = {}
    for character in lowered:
        if character in character_count: 
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count

########## WORKING BELOW ############
def character_count_dict_to_list(character_count):
    char_list = []
    for character in character_count:
        char_list.append({"char": character, "num": character_count[character]})
    char_list.sort(reverse=True, key=sort_by)
    return char_list

def sort_by(char_list):
    return char_list["num"]
