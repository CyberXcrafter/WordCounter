def word_counter(text):

    word_count = len(text.split())

    character_count = len(text)

    sentence_count = text.count('.') + text.count('!') + text.count('?')

    return word_count, character_count, sentence_count

def main():
    user_text = input("Enter your text: ")
    words, chars, sentences = word_counter(user_text)

    print(f"\nNumber of words: {words}")
    print(f"Number of characters: {chars}")
    print(f"Number of sentences: {sentences}")

if __name__ == "__main__":
    main()
