from openai import OpenAI

# Contact SohamGlobal 73919 66656 for API key if you don't have one
client = OpenAI(api_key="your_api_key_here")

with open("granth.mp3", "rb") as f:
    transcript = client.audio.transcriptions.create(
        file=f,
        model="gpt-4o-transcribe"
    )

print("You said:", transcript.text)
