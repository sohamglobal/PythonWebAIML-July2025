from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

endpoint = "https://sohamsentiments.cognitiveservices.azure.com/"
key = ""

client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

cont="""
I am a big fan of volkswagen cars. this is amazing. it has great looks and it is sturdy.
it is little expensive but tiguan is the best for my family.
"""

documents = [cont]

response = client.analyze_sentiment(documents=documents)

for doc in response:
    print(doc.sentiment, doc.confidence_scores)
