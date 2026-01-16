from openai import OpenAI

# Contact SohamGlobal 73919 66656 for API key if you don't have one
client = OpenAI(api_key="your_api_key_here")


text_to_read = "Hello! Welcome to SohamGlobal, we help you build your profile for success."

# ---- Text to Speech ----
speech = client.audio.speech.create(
    model="gpt-4o-mini-tts",
    voice="alloy",
    input=text_to_read
)

# ---- SAVE AUDIO (IMPORTANT FIX) ----
with open("output.mp3", "wb") as f:
    f.write(speech.read())

print("Voice output saved as output.mp3")

