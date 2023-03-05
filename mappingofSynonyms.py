import nltk
nltk.download('wordnet')

from nltk.corpus import wordnet

def generate_synonyms(input_phrase):
    synonyms = []

    for word in input_phrase.split():
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                synonym = lemma.name()
                pos = lemma.synset().pos()

                if pos.startswith('N'):
                    wn_pos = wordnet.NOUN
                elif pos.startswith('V'):
                    wn_pos = wordnet.VERB
                elif pos.startswith('J'):
                    wn_pos = wordnet.ADJ
                elif pos.startswith('R'):
                    wn_pos = wordnet.ADV
                else:
                    wn_pos = wordnet.NOUN

                for syn2 in wordnet.synsets(synonym, pos=wn_pos):
                    for lemma2 in syn2.lemmas():
                        synonym2 = lemma2.name().replace('_', ' ')
                        if synonym2 != input_phrase and synonym2 not in synonyms:
                            synonyms.append(synonym2)

    print(synonyms)
