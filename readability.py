from cs50 import get_string

def main():
    text = get_string("Text: ")

    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    L = (letters / words) * 100
    S = (sentences / words) * 100

    index = calculate_index(L, S)
    grade = get_grade(index)

    print(f"Grade {grade}")

def count_letters(text):
    count = 0
    for char in text:
        if char.isalpha():
            count += 1
    return count

def count_words(text):
    count = 0
    words = text.split()
    count = len(words)
    return count

def count_sentences(text):
    count = 0
    for char in text:
        if char in ['.', '!', '?']:
            count += 1
    return count

def calculate_index(L, S):
    return 0.0588 * L - 0.296 * S - 15.8

def get_grade(index):
    grade = round(index)
    if grade >= 16:
        return "16+"
    elif grade < 1:
        return "Before Grade 1"
    else:
        return str(grade)

if __name__ == "__main__":
    main()
