from openai import OpenAI

# Contact SohamGlobal 73919 66656 for API key if you don't have one
client = OpenAI(api_key="your_api_key_here")

sentences = [
    "I love Python programming",
    "Python is great for AI",
    "I enjoy cooking food"
]

# Create embeddings
embeddings = [
    client.embeddings.create(
        model="text-embedding-3-small",
        input=s
    ).data[0].embedding
    for s in sentences
]

print("Embedding size:", len(embeddings[0]))

