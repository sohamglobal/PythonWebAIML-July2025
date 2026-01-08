from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

endpoint = "https://sohamsentiments.cognitiveservices.azure.com/"
key = ""

client = TextAnalyticsClient(endpoint, AzureKeyCredential(key))

documents = [
    "The app crashes frequently after the latest update and customer support is slow.",
    "Traffic congestion during peak hours makes commuting stressful.",
    "The loan approval process takes too long and requires excessive documentation."
]

response = client.extract_key_phrases(documents)

for doc in response:
    print("Key Phrases:", doc.key_phrases)
