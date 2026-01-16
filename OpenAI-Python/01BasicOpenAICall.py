# pip install openai
from openai import OpenAI

# Contact SohamGlobal 73919 66656 for API key if you don't have one
client = OpenAI(api_key="your_api_key_here")


response = client.chat.completions.create(
    model="gpt-5",
    messages=[
        {"role":"system","content":"You are a helpful technical assistant."},
        {"role":"user","content":"Tell me about importance of ethical frameworks in AI. Give me 5 points."}
    ],
)

print(response.choices[0].message.content)

