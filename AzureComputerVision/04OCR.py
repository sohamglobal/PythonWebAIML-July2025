from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

# ---------------------------------
# Azure credentials
# ---------------------------------
endpoint = "https://sohamvision.cognitiveservices.azure.com/"
key = "apikey"

client = ImageAnalysisClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)

# ---------------------------------
# Local image
# ---------------------------------
image_path = "menu.jpg"   # image containing text

with open(image_path, "rb") as f:
    image_data = f.read()

# ---------------------------------
# Analyze image for OCR (TEXT)
# ---------------------------------
result = client.analyze(
    image_data=image_data,
    visual_features=[VisualFeatures.READ]
)

# ---------------------------------
# Print extracted text
# ---------------------------------
print("Extracted Text:")

for block in result.read.blocks:
    for line in block.lines:
        print(line.text)
