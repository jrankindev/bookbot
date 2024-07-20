def read_book(path):
    with open(path) as file:
        file_contents = file.read()
    return file_contents

def count_words(text):
    count = len(text.split())
    return count

def count_letters(text):
    text = text.lower()
    letter_counts = {}

    for char in text:
        if char.isalpha():
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1

    sorted_letter_counts = dict(sorted(letter_counts.items(), key=lambda item: item[1], reverse=True))
    return sorted_letter_counts

def generate_report(path, word_count, letter_count):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")
    for letter, count in letter_count.items():
        print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")

def main():
    book_path = "books/frankenstein.txt"
    book_text = read_book(book_path)

    word_count = count_words(book_text)
    letter_count = count_letters(book_text)

    generate_report(book_path, word_count, letter_count)

if __name__ == "__main__":
    main()
