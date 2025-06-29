import sys
from stats import get_num_words, get_char_count, sort_dict

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")

    print("----------- Word Count ----------")
    text = get_book_text(filepath)
    print(f"Found {get_num_words(text)} total words")

    print("--------- Character Count -------")
    char_counts = sort_dict(get_char_count(text))
    for char in char_counts:
        c = char["char"]
        if c.isalpha() is True:
            n = char["num"]
            print(f"{c}: {n}")

    print("============= END ===============")

def get_book_text(filepath):
    text = None
    with open(filepath) as f:
        text = f.read()
    return text

main()