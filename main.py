import sys 

def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text

from stats import get_word_count
from stats import get_character_count
from stats import character_count_dict_to_list


def main():
    
    book = get_book_text(sys.argv[1])
    word_count = get_word_count(book)
    character_count = get_character_count(book)
    sorted_characters = character_count_dict_to_list(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_characters:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")
    print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
main()

