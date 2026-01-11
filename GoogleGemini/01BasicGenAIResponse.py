# pip install -q -U google-genai
'''
import os

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
'''
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Explain how AI works in 3 lines",
)

print(response.text)