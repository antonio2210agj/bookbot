import sys
from stats import number_of_words
from stats import character_appearances
from stats import sort_dict

def get_book_text(path_to_file):
    with open(path_to_file, encoding="utf-8") as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")

    book_text = get_book_text(path_to_file)

    print("----------- Word Count ----------")
    print(number_of_words(book_text))

    print("--------- Character Count -------")
    sorted_characters = sort_dict(character_appearances(book_text))
    for character in sorted_characters:
        print(f"{character['char']}: {character['num']}")

    print("============= END ===============")

main()
