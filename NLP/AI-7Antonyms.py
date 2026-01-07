from nltk.corpus import wordnet

word = "good"

antonyms = set()

for syn in wordnet.synsets(word):
    for lemma in syn.lemmas():
        if lemma.antonyms():
            antonyms.add(lemma.antonyms()[0].name())

print("Antonyms:", antonyms)
