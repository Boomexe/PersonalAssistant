import nltk

def download_punkt():
    nltk.download('punkt')

# download_punkt()

def tokenize(sentence: str) -> list:
    return nltk.word_tokenize(sentence)