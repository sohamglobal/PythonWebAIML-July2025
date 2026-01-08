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

# Input text
documents = [
    "The battery life is excellent but the camera quality is poor."
]

# Call sentiment analysis with opinion mining enabled
response = client.analyze_sentiment(
    documents,
    show_opinion_mining=True
)

# Process results
for doc in response:
    print("Overall Sentiment:", doc.sentiment)
    print("Confidence Scores:", doc.confidence_scores)

    for sentence in doc.sentences:
        for opinion in sentence.mined_opinions:
            target = opinion.target
            print(f"\nAspect: {target.text}")
            print(f"  Sentiment: {target.sentiment}")

            for assessment in opinion.assessments:
                print(f"  Opinion: {assessment.text}")
                print(f"  Opinion Sentiment: {assessment.sentiment}")
