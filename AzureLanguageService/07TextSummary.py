from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

endpoint = "https://sohamsentiments.cognitiveservices.azure.com/"
key = ""

client = TextAnalyticsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)

documents = [
    """Online education has grown rapidly in recent years.
    It provides flexibility for students to learn from anywhere.
    However, lack of face-to-face interaction and practical exposure can be challenging.
    Despite this, online learning remains a popular choice due to its convenience and affordability."""
]

# Start extractive summarization
poller = client.begin_extract_summary(documents, max_sentence_count=2)
result = poller.result()

print("Summary:\n")

for doc in result:
    for sentence in doc.sentences:
        print("-", sentence.text)
