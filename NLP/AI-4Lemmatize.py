from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()


print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("formulae"))
print(lemmatizer.lemmatize("syllabi"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("rocks"))
