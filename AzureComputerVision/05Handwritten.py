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
# Local handwritten image
# ---------------------------------
image_path = "music.jpeg"

with open(image_path, "rb") as f:
    image_data = f.read()

# ---------------------------------
# Analyze image for READ (OCR)
# ---------------------------------
result = client.analyze(
    image_data=image_data,
    visual_features=[VisualFeatures.READ]
)

# ---------------------------------
# Print recognized handwritten text
# ---------------------------------
print("Recognized Handwritten Text:")

for block in result.read.blocks:
    for line in block.lines:
        print(line.text)
