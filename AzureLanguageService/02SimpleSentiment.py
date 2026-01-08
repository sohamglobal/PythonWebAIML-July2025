from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

endpoint = "https://sohamsentiments.cognitiveservices.azure.com/"
key = ""

client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

documents = ["I love this product!", "Not happy with the service."]

response = client.analyze_sentiment(documents=documents)

for doc in response:
    print(doc.sentiment, doc.confidence_scores)
