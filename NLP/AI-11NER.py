# pip install spacy
# python -m spacy download en_core_web_sm

import spacy

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

text="""
Praffull is the co-founder of SohamGlobal. He lives in India. 
He founded the company in 2004. It is a Microsoft and AWS partner company.
"""

# Process the text
doc = nlp(text)

# Print named entities
for ent in doc.ents:
    print(ent.text, "->", ent.label_)
