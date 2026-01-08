from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Azure credentials
endpoint = "https://sohamsentiments.cognitiveservices.azure.com/"
key = ""

client = TextAnalyticsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)

# Sample social media posts
tweets = [
    "Absolutely loving the cool weather this morning, perfect start to the day!",
    "The traffic today was unbearable, took forever to reach the office.",
    "The new phone update is decent, some features are useful while others feel unnecessary.",
    "Feeling grateful for supportive friends and family during tough times.",
    "Customer service was slow and unhelpful, very disappointing experience."
]


# Analyze sentiment
response = client.analyze_sentiment(tweets)

# Counters
summary = {"positive": 0, "neutral": 0, "negative": 0}

print("Social Media Sentiment Report\n")

for tweet, result in zip(tweets, response):
    print(f"Post: {tweet}")
    print(f"Sentiment: {result.sentiment}")
    print(f"Scores: {result.confidence_scores}\n")

    summary[result.sentiment] += 1

# Final summary
print("Overall Sentiment Summary")
for k, v in summary.items():
    print(f"{k.capitalize()}: {v}")
