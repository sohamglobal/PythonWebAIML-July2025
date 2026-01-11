from PIL import Image
from google import genai

client = genai.Client()

image = Image.open("instrument.jpg")
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[image, "Tell me about this instrument"]
)
print(response.text)