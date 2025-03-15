from stats import get_number_of_words,get_number_of_characters,get_sorted_dictionary

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def print_stats(filepath,num_words,sorted_character_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for d in sorted_character_dict:
        if d['letter'].isalpha():
          print(f"{d['letter']}: {d['num']}")
    print("============= END ===============")

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    file_contents = get_book_text(filepath)
    num_words = get_number_of_words(file_contents)
    character_list = get_number_of_characters(file_contents)
    sorted_character_dict = get_sorted_dictionary(character_list)
    print_stats(filepath,num_words,sorted_character_dict)

main()