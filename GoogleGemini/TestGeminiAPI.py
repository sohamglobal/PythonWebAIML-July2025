from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Give me one paragraph of information on history of computers",
)

print(response.text)