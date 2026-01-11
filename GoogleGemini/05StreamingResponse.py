from google import genai

client = genai.Client()

response = client.models.generate_content_stream(
    model="gemini-2.5-flash",
    contents=["How cricket is played?"]
)
for chunk in response:
    print(chunk.text, end="")