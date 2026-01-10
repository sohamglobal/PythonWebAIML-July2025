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
image_path = "coco.jpg"

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
# Print detected objects
# ---------------------------------
print("Detected Objects:")

for obj_list in result.objects.values():
    for obj in obj_list:
        box = obj.bounding_box

        # Object label comes from tags
        label = obj.tags[0].name
        confidence = obj.tags[0].confidence

        print(
            f"- {label} "
            f"(confidence: {round(confidence, 2)}) "
            f"[x={box.x}, y={box.y}, w={box.width}, h={box.height}]"
        )