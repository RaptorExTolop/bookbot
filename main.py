file_contents = None

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_count = count_words(file_contents)
    print(word_count)
    print(count_chars(file_contents))

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
            NOEC[i] = 0
    return NOEC

main()