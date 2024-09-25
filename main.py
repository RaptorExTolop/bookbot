file_contents = None

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_count = count_words(file_contents)
    print(word_count)

def count_words(c):
    total_words = 0
    c = c.split()
    for i in range(len(c)):
        total_words += 1
    return total_words

main()