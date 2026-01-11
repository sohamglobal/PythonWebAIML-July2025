from google import genai
from google.genai import types
from PIL import Image

client = genai.Client()

image_input = Image.open('/path/to/your/man_in_white_glasses.jpg')
text_input = "Make a 3 panel comic in a gritty, noir art style with high-contrast black and white inks. Put the character in a humurous scene."

response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents=[text_input, image_input],
)

for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = part.as_image()
        image.save("comic_panel.jpg")