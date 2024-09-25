file_contents = None

def main():
    text_name = "frankenstein"
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_count = count_words(file_contents)
    counted_chars = count_chars(file_contents)
    book_report(text_name, word_count, counted_chars)

def count_words(c):
    total_words = 0
    c = c.split()
    for i in range(len(c)):
        total_words += 1
    return total_words

def count_chars(text):
    no_of_chars = {} # Numbers Of Each Chars
    for char in text:
        if char == ' ' or char == '\n':
            pass
        elif char in no_of_chars:
            no_of_chars[char] += 1
        else:
            no_of_chars[char] = 1
    return no_of_chars

def book_report(name, words, chars):
    print(f"--- Begin report of {name} ---")
    print(f"{words} words found in the document")
    print()
    for i in chars:
        print(f"The '{i}' character was found {chars[i]} times")
    print("--- end report ---")

main()