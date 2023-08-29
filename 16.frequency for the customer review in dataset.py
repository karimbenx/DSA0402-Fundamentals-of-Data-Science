import pandas as pd
import string
from collections import Counter
import matplotlib.pyplot as plt

# Load the dataset from a CSV file (replace with your CSV file)
csv_file_path = r"C:\Users\Merwin S\OneDrive\Desktop\python\data.csv"
df = pd.read_csv(csv_file_path)

# Preprocess text
translator = str.maketrans("", "", string.punctuation)

def preprocess_text(text):
    text = text.lower()
    text = text.translate(translator)
    tokens = text.split()
    return [token for token in tokens]

# Preprocess and tokenize the entire dataset
preprocessed_tokens = []
for review in df["Feedback"]:
    cleaned_tokens = preprocess_text(review)
    preprocessed_tokens.extend(cleaned_tokens)

# Calculate frequency distribution of words
word_freq = Counter(preprocessed_tokens)

# Get user input for the number of top words to display
try:
    n = int(input("Enter the number of top words to display: "))
except ValueError:
    print("Invalid input. Using default value of 10.")
    n = 10

# Display the top N most frequent words and their frequencies
print(f"Top {n} Most Frequent Words:")
for word, freq in word_freq.most_common(n):
    print(f"{word}: {freq}")

# Visualize the distribution using a bar plot
top_words = [word for word, _ in word_freq.most_common(n)]
top_word_freq = [word_freq[word] for word in top_words]

plt.figure(figsize=(12, 6))
plt.bar(top_words, top_word_freq)
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title(f"Top {n} Most Frequent Words in Customer Reviews")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
