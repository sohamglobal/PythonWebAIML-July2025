from nltk.corpus import wordnet

word = "good"

synonyms = set()

for syn in wordnet.synsets(word):
    for lemma in syn.lemmas():
        synonyms.add(lemma.name())

print("Synonyms:", synonyms)
print("Total Synonyms Found:", len(synonyms))