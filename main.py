import sys
from stats import count_words, count_characters, sort_character_counts

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    book_path = sys.argv[1]
    book_content = get_book_text(book_path)
    num_words = count_words(book_content)
    char_counts = count_characters(book_content)
    sorted_chars = sort_character_counts(char_counts)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        char = list(char_dict.keys())[0]
        count = char_dict[char]
        print(f"{char}: {count}")
    print("============= END ===============")



main()
