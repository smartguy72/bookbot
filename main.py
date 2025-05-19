def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text

from stats import get_word_count

from stats import get_character_count

def main():
    book = get_book_text("books/frankenstein.txt")
    word_count = get_word_count(book)
    character_count = get_character_count(book)
    print(f"{word_count} words found in the document")
    print(character_count)
main()
