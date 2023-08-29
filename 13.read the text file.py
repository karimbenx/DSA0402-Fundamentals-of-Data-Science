import string
from collections import Counter

def clean_text(text):
    # Remove punctuation and convert to lowercase
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = text.lower()
    return text

def calculate_word_frequencies(tokens):
    word_freq = Counter(tokens)
    return word_freq

def main():
    # Read the text from the file
    with open("C:/Users/Merwin S/OneDrive/Desktop/List, which is used to store multip.txt", "r") as file:
        text = file.read()

    # Clean and tokenize the text
    cleaned_text = clean_text(text)
    tokens = cleaned_text.split()

    # Calculate word frequencies
    word_freq = calculate_word_frequencies(tokens)

    # Sort the frequency distribution
    sorted_word_freq = dict(sorted(word_freq.items(), key=lambda item: item[1], reverse=True))

    # Display the frequency distribution
    for word, freq in sorted_word_freq.items():
        print(f"{word}: {freq}")

if __name__ == "__main__":
    main()
