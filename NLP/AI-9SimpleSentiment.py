# pip install textblob

from textblob import TextBlob

text = "I love learning Python and AI"

blob = TextBlob(text)
print(blob.sentiment)

text = "I don't like going to school and doing homework"

blob = TextBlob(text)
print(blob.sentiment)

text = "I hate religion to be used in politics"

blob = TextBlob(text)
print(blob.sentiment)