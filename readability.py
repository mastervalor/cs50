def count_letters(text):
    letters = 0
    for char in text:
        if char.isalpha():
            letters += 1
    return letters


def count_words(text):
    words = 1
    for char in text:
        if char.isspace():
            words += 1
    return words


def count_sentences(text):
    sentences = 0
    for char in text:
        if char in [".", "?", "!"]:
            sentences += 1
    return sentences


def get_grade(l, w, s):
    avg_l = (l / w) * 100
    avg_s = (s / w) * 100
    index = 0.0588 * avg_l - 0.296 * avg_s - 15.8
    return round(index)


def main():
    text = input("Text: ")
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)
    grade = get_grade(letters, words, sentences)

    if grade >= 16:
        print("Grade 16+")
    elif grade <= 0:
        print("Before Grade 1")
    else:
        print(f"Grade {grade}")


if __name__ == "__main__":
    main()
