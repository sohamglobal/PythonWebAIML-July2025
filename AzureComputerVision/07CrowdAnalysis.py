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
# Local image (classroom / crowd)
# ---------------------------------
image_path = "england.jpg"

with open(image_path, "rb") as f:
    image_data = f.read()

# ---------------------------------
# Analyze image for OBJECTS
# ---------------------------------
result = client.analyze(
    image_data=image_data,
    visual_features=[VisualFeatures.OBJECTS]
)

# ---------------------------------
# Count people
# ---------------------------------
people_count = 0

for obj_list in result.objects.values():
    for obj in obj_list:
        # Object label is inside tags
        label = obj.tags[0].name.lower()
        if label == "person":
            people_count += 1

print("Total People Detected:", people_count)
