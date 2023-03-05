import nltk
nltk.download('wordnet')

from nltk.corpus import wordnet

input_word = 'Heated Apparel'

input_words = input_word.split()

synonyms = []

for word in input_words:
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            if lemma.name() != word and lemma.name() not in synonyms:
                synonyms.append(lemma.name())

print(synonyms)
