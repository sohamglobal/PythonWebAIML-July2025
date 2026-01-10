# pip install azure-ai-vision-imageanalysis

from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

#  Azure details
endpoint = "https://sohamvision.cognitiveservices.azure.com/"
key = "apikey"

# Create client
client = ImageAnalysisClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)

# Path to LOCAL image
image_path = "rg.jpg"

# Read image as bytes
with open(image_path, "rb") as image_file:
    image_data = image_file.read()

# Analyze image
result = client.analyze(
    image_data=image_data,
    visual_features=[VisualFeatures.CAPTION]
)

# Output caption
if result.caption:
    print("Image Caption:")
    print(result.caption.text)
    print("Confidence:", round(result.caption.confidence, 2))
else:
    print("No caption generated")