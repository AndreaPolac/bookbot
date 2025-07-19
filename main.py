from stats import get_num_words, get_book_text, count_characters, sort_char_dictionary
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_words = get_num_words(filepath)
    char_count_dict = count_characters(text)
    print(f"Found {num_words} total words")
    sorted_dict = sort_char_dictionary(char_count_dict)
    for item in sorted_dict:
        print(f"{item['char']}: {item['num']}")

main()
