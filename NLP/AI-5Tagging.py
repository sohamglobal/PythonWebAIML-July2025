import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

#train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("1945-Truman.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(sample_text)
print(custom_sent_tokenizer)
tokenized = custom_sent_tokenizer.tokenize(sample_text)
#print(tokenized)


def process_content():
    try:
        for i in tokenized[:1]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)

    except Exception as e:
        print(str(e))


process_content()
