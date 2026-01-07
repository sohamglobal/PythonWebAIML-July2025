from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
   
ps = PorterStemmer() 
  
# choose some words to be stemmed 
#words = ["program", "programs", "programmer", "programming", "programmers"] 
words=['store','storing','stored','stores'] 
#words=['killed','killing','killer','kill']
 
for w in words: 
    print(w, " : ", ps.stem(w)) 