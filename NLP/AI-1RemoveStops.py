#pip install nltk
#>>> import nltk
#>>> nltk.download()

from nltk import word_tokenize as wt
from nltk.corpus import stopwords
from nltk.corpus import state_union


text="""My name is Ethan Hunt. I follow Chelsea football club. 
I also do python programming."""


#text=state_union.raw("1945-Truman.txt")
a=set(stopwords.words('english'))
#print(a)

text1=wt(text.lower())
print(text1)

print('----------------Stop words---------------------')

words=[x for x in text1 if x in a]
print(words)



print('----------------Stops Removed---------------------')

words=[x for x in text1 if x not in a]
print(words)
