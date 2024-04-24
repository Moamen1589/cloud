import nltk
from nltk.corpus import stopwords
from collections import Counter
import string

nltk.download('punkt')
nltk.download('stopwords')

def remove_stopwords_and_count_frequency(text):
    stop_words = set(stopwords.words('english'))
    words = nltk.word_tokenize(text.lower())  # Tokenize and convert to lowercase
    words = [word.strip(string.punctuation) for word in words]  # Remove punctuation
    filtered_words = [word for word in words if word not in stop_words]
    word_freq = Counter(filtered_words)
    return word_freq

# Read text from file
with open('paragraphs.txt', 'r') as file:
    text = file.read()

# Remove stop words and count frequency
word_freq = remove_stopwords_and_count_frequency(text)

# Print word frequencies
for word, freq in word_freq.items():
    print(f"{word}: {freq}")

