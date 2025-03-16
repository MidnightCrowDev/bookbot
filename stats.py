def get_books_text(book_path):
    try:
        with open(book_path, 'r', encoding='utf-8') as f:
            file_contents = f.read()
            return file_contents
    except FileNotFoundError:
        print(f"Error: File not found at path: {book_path}")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def get_word_count(book_path):
    file_contents = get_books_text(book_path)
    if file_contents:
        words = file_contents.split()
        return len(words)
    else:
        return 0

def character_repeat_counter(book_path):
    char_dict = {}
    book_text = get_books_text(book_path)
    if book_text:
        small_book = book_text.lower()
        for char in small_book:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def sorted_char_dict(char_dict):
    unsorted_dict = []
    for key, value in char_dict.items():
        new_dict = {}
        new_dict["char"] = key
        new_dict["count"] = value
        unsorted_dict.append(new_dict)

    def sort_on(dict):
        return dict["count"]

    unsorted_dict.sort(reverse=True, key=sort_on)
    return unsorted_dict
