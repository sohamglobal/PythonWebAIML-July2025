from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Azure credentials
endpoint = "https://sohamsentiments.cognitiveservices.azure.com/"
key = ""

# Create client
client = TextAnalyticsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)

# Sample texts in different languages
documents = [
    "This is a wonderful day",
    "यह सेवा बहुत अच्छी है",
    "Este servicio es excelente",
    "Ce service est très bon"
]

# Detect language
response = client.detect_language(documents)

print("Language Detection Results\n")

for text, result in zip(documents, response):
    print(f"Text: {text}")
    print(f"Detected Language: {result.primary_language.name}")
    print(f"Language Code: {result.primary_language.iso6391_name}")
    print(f"Confidence Score: {result.primary_language.confidence_score}\n")
