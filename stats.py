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


