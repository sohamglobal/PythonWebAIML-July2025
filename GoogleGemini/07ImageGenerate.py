from google import genai
from google.genai import types
from PIL import Image

client = genai.Client()

prompt = ("Create an image of a futuristic cityscape at sunset with flying cars and towering skyscrapers.")
response = client.models.generate_content(
    model="gemini-2.5-flash-image",
    contents=[prompt],
)

for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = part.as_image()
        image.save("generated_image.png")