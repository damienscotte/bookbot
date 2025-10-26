import sys
from stats import count_words, count_characters, sort_characters


def get_book_text(path_to_file):
    with open(path_to_file, 'r', encoding='utf-8') as f:
        return f.read()


def main():
    # Vérifier qu'un argument a bien été fourni
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")

    num_words = count_words(text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")

    char_dict = count_characters(text)
    sorted_chars = sort_characters(char_dict)

    for item in sorted_chars:
        ch = item["char"]
        num = item["num"]
        print(f"{ch}: {num}")

    print("============= END ===============")


if __name__ == "__main__":
    main()

