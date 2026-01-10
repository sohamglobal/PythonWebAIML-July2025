from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

# -----------------------------
# Azure credentials
# -----------------------------

endpoint = "https://sohamvision.cognitiveservices.azure.com/"
key = "apikey"

client = ImageAnalysisClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)

# -----------------------------
# Local image path
# -----------------------------
image_path = "pmedium.jpg"   # Replace with your local image

# -----------------------------
# Read image bytes
# -----------------------------

with open(image_path, "rb") as f:
    image_data = f.read()

# Analyze image for TAGS
result = client.analyze(
    image_data=image_data,
    visual_features=[VisualFeatures.TAGS]
)

# ✅ Correct way to print tags
print("Detected Tags:")

for tag_list in result.tags.values():      # tag_list is a LIST
    for tag in tag_list:                   # tag is a TagResult
        print(f"- {tag.name} (confidence: {round(tag.confidence, 2)})")

