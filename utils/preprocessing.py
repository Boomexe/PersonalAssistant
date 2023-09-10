import nltk
from nltk.stem.porter import PorterStemmer
import numpy as np

def download_punkt():
    nltk.download('punkt')

# download_punkt()

def lowercase_text(text: str) -> str:
    return text.lower()

def stem(word: str) -> str:
    stemmer = PorterStemmer()
    
    return stemmer.stem(lowercase_text(word))

def bag_of_words(tokenized_sentence: list, all_words: list):
    tokenized_sentence = [stem(w) for w in tokenized_sentence]
    
    bag = np.zeros(len(all_words), dtype=np.float32)

    for index, w, in enumerate(all_words):
        if w in tokenized_sentence:
            bag[index] = 1.0
    
    return bag