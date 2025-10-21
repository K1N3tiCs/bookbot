from stats import get_book_text, get_total_words, get_total_characters, sort_on_1 # ,helper
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print('=' * 11 + " BOOKBOT " + '=' * 11)
    file_path = sys.argv[1]
    file_content = get_book_text(file_path)
    print(get_total_words(file_content))
    (sort_on_1(get_total_characters(file_content)))
    print('-' * 11 + 'END' + '-' * 11)
    # print(helper(get_total_characters(file_content)))

main()
