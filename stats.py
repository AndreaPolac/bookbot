def get_book_text(filepath: str) -> str:
    with open(filepath) as file:
        return file.read()

def count_words(text: str) -> int:
    """Return the number of words in the given text."""
    return len(text.split())

def get_num_words(filepath: str) -> int:
    """Return the number of words in the book located at filepath."""
    book_text = get_book_text(filepath)
    return count_words(book_text)

def count_characters(text: str) -> dict:
    """Return a dictionary with the count of each character (lowercased) in the text."""
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def transform_char_count_dict(char_count_dict: dict) -> dict:
    return [
        {"char": char, "num": num} for char, num in char_count_dict.items() if char.isalpha()
    ]

def sort_char_dictionary(char_count_dict: dict) -> list:
    transfomred_dict = transform_char_count_dict(char_count_dict)
    transfomred_dict.sort(reverse=True, key=lambda item: item["num"])
    return transfomred_dict