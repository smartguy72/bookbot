def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text
def main():
    book = get_book_text("books/frankenstein.txt")
    print(book)
main()
