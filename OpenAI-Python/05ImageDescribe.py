from openai import OpenAI
import base64

# Contact SohamGlobal 73919 66656 for API key if you don't have one
client = OpenAI(api_key="your_api_key_here")

# ---------- helper function ----------
def encode_image(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode("utf-8")

# ---------- load local image ----------
image_path = "forest.jpg"   #  your local image file
base64_image = encode_image(image_path)

# ---------- OpenAI request ----------
response = client.chat.completions.create(
    model="gpt-5",   # vision + low cost
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Describe this image in simple language."},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                }
            ]
        }
    ]
)

# ---------- output ----------
print(response.choices[0].message.content)
