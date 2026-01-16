from openai import OpenAI
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

# Contact SohamGlobal 73919 66656 for API key if you don't have one
client = OpenAI(api_key="your_api_key_here")

# ---------------------------------
# 1. Record voice from microphone
# ---------------------------------
duration = 5          # seconds
sample_rate = 16000   # required for speech-to-text

print("Speak your sentence...")
audio = sd.rec(int(duration * sample_rate),
               samplerate=sample_rate,
               channels=1,
               dtype="int16")
sd.wait()
print("Recording finished")

# Save temp wav file
write("input.wav", sample_rate, audio)

# ---------------------------------
# 2. Speech → Text
# ---------------------------------
with open("input.wav", "rb") as audio_file:
    transcription = client.audio.transcriptions.create(
        file=audio_file,
        model="gpt-4o-transcribe"
    )

original_text = transcription.text
print("\nOriginal Text:")
print(original_text)

# ---------------------------------
# 3. Tone Transformation
# ---------------------------------
target_tone = "polite"   # try: formal, friendly, professional, humorous

response = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {
            "role": "system",
            "content": f"You rewrite sentences in a {target_tone} tone."
        },
        {
            "role": "user",
            "content": original_text
        }
    ]
)

transformed_text = response.choices[0].message.content
print(f"\nTransformed Text ({target_tone} tone):")
print(transformed_text)

# ---------------------------------
# 4. Text → Speech (Play directly)
# ---------------------------------
speech = client.audio.speech.create(
    model="gpt-4o-mini-tts",
    voice="alloy",
    input=transformed_text,
    response_format="wav"
)

audio_bytes = speech.read()
audio_np = np.frombuffer(audio_bytes, dtype=np.int16)

sd.play(audio_np, samplerate=24000)
sd.wait()

print("\nTransformed voice played successfully")
