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

def count_chars(c):
    NOEC = {} # Numbers Of Each Chars
    for i in c:
        if i == ' ' or i == '\n':
            pass
        elif i in NOEC:
            NOEC[i] += 1
        else:
            NOEC[i] = 1
    return NOEC

def book_report(x, y, z):
    print(f"--- Begin report of {x} ---")
    print(f"{y} words found in the document")
    print()
    for i in z:
        print(f"The '{i}' character was found {z[i]} times")
    print("--- end report ---")

main()