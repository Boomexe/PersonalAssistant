from nltk.corpus import wordnet

patterns = ['define', 'definition', 'what', 'is', 'the', 'mean', 'meaning', 'of', 'word', 'do', 'you', 'know', 'does']

def main(*args):
    sentence = args[0][0]
    ask_sentence = []
    for word in sentence:
        if word not in patterns:
            ask_sentence.append(word)
    
    if len(ask_sentence) > 0:
        try:
            ask_word = ask_sentence[0]
            
            syn = wordnet.synsets(ask_word)[0]
            definition = syn.definition()

            return f'The definition of {ask_word} is {definition}.'

        except(IndexError):
            return 'Did not understand'
    
    return 'Did not understand.'