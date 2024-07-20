def main():
    with open("books/frankenstein.txt") as file:
        file_contents = file.read()

        
        word_count(file_contents)

def word_count(words):
    count = len(words.split())
    print(count)
    return count

main()
