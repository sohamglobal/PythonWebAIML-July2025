import string

text = "Hello!!! Welcome to NLP, Python :)"

clean_text = text.translate(str.maketrans("", "", string.punctuation))
print(clean_text)
