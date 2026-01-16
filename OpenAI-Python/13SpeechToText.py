# pip install openai sounddevice scipy

from openai import OpenAI
import sounddevice as sd
from scipy.io.wavfile import write

# Contact SohamGlobal 73919 66656 for API key if you don't have one
client = OpenAI(api_key="your_api_key_here")

# ----------------------------
# Record audio from microphone
# ----------------------------
duration = 5        # seconds
sample_rate = 16000 # required for speech models

print("Speak now...")
audio = sd.rec(int(duration * sample_rate),
                samplerate=sample_rate,
                channels=1,
                dtype="int16")
sd.wait()
print("Recording finished")

# Save temporary wav file
write("input.wav", sample_rate, audio)

# ----------------------------
# Speech → Text (OpenAI)
# ----------------------------
with open("input.wav", "rb") as audio_file:
    transcription = client.audio.transcriptions.create(
        file=audio_file,
        model="gpt-4o-transcribe"
    )

print("\n📝 Transcribed Text:")
print(transcription.text)

