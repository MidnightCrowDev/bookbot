import sys
from stats import get_word_count
from stats import get_books_text
from stats import character_repeat_counter
from stats import sorted_char_dict

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_books_text(book_path)
    book_word_count = get_word_count(book_path)

    report = f"""============ BOOKBOT ============
    Analyzing book found at {book_path}...
    ----------- Word Count ----------
    Found {book_word_count} total words
    --------- Character Count -------"""
    print(report)

    char_dict = character_repeat_counter(book_path)
    sorted_chars = sorted_char_dict(char_dict)

    for char_info in sorted_chars:
        char = char_info["char"]
        count = char_info["count"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
