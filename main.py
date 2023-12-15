def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words_count = len(file_contents.split())
        letters_count = letters(file_contents)
        print_report(words_count, letters_count)


def letters(text):
    letters_dict = {}
    for char in text.lower():
        if not char.isalpha():
            continue
        if char not in letters_dict:
            letters_dict[char] = 1
        else:
            letters_dict[char] += 1
    return letters_dict


def print_report(word_count, letters):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print()

    letters_items = list(letters.items())
    letters_items.sort(key=lambda x: x[1], reverse=True)
    for item in letters_items:
        print(f"The '{item[0]}' was found {item[1]} times")

    print("--- End report ---")


main()
