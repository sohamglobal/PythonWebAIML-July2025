from openai import OpenAI
import sounddevice as sd
from scipy.io.wavfile import write

# Contact SohamGlobal 73919 66656 for API key if you don't have one
client = OpenAI(api_key="your_api_key_here")

# ----------------------------
# 1. Record Hindi speech
# ----------------------------
duration = 10          # seconds
sample_rate = 16000   # required

print("Hindi mein boliye...")
audio = sd.rec(int(duration * sample_rate),
                samplerate=sample_rate,
                channels=1,
                dtype="int16")
sd.wait()
print("Recording finished")

# Save temporary audio file
write("hindi_input.wav", sample_rate, audio)

# ----------------------------
# 2. Speech → Text (Hindi)
# ----------------------------
with open("hindi_input.wav", "rb") as audio_file:
    transcription = client.audio.transcriptions.create(
        file=audio_file,
        model="gpt-4o-transcribe"
    )

hindi_text = transcription.text
print("\nHindi Text:")
print(hindi_text)

# ----------------------------
# 3. Hindi → English Translation
# ----------------------------
response = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {"role": "system", "content": "You translate Hindi to English accurately."},
        {"role": "user", "content": f"Translate this Hindi text to English:\n{hindi_text}"}
    ]
)

english_text = response.choices[0].message.content

print("\nEnglish Translation:")
print(english_text)
