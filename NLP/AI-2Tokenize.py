from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize

text="""Jofra Archer and Mark Wood are set to be paired together for the first time overseas 
later this week at a time when England captain Eoin Morgan believes the global game 
s witnessing a renaissance of genuinely fast bowling."""

print('------------ Text Tokenization ----------------')

token=word_tokenize(text)
print(token)

print('------------ Frequency finding of Tokens ----------------')
fdist=FreqDist(token)
print(fdist)

print('------------ Top most 10 common tokens ----------------')

fdist1=fdist.most_common(10)
print(fdist1)