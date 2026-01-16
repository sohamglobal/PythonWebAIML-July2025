from openai import OpenAI

# Contact SohamGlobal 73919 66656 for API key if you don't have one
client = OpenAI(api_key="your_api_key_here")

document = open("work-from-home.txt").read()
question = "What are the key benefits mentioned?"

response = client.chat.completions.create(
    model="gpt-5",
    messages=[
        {"role":"system","content":"You are a helpful assistant."},
        {"role":"user","content":f"Document:\n{document}\n\nQ: {question}"}
    ],
)

print(response.choices[0].message.content)

