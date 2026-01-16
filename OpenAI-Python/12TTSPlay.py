# pip install sounddevice numpy

from openai import OpenAI
import sounddevice as sd
import numpy as np

# Contact SohamGlobal 73919 66656 for API key if you don't have one
client = OpenAI(api_key="your_api_key_here")

text_to_read = """
The meeting commenced with the Regional Sales Manager welcoming 
all participants and outlining the agenda. The primary focus was 
to review Q4 sales performance, discuss strategies for boosting 
market share in Tier-2 and Tier-3 cities, and evaluate the 
effectiveness of recent promotional campaigns. The team agreed to 
also address customer feedback trends and upcoming product launches scheduled for Q1 2026.
"""

# ---- Generate speech (CORRECT PARAMETER) ----
speech = client.audio.speech.create(
    model="gpt-4o-mini-tts",
    voice="alloy",
    input=text_to_read,
    response_format="wav"   
)

# ---- Read raw audio bytes ----
audio_bytes = speech.read()

# ---- Convert to numpy array ----
audio_np = np.frombuffer(audio_bytes, dtype=np.int16)

# ---- Play audio ----
sd.play(audio_np, samplerate=24000)
sd.wait()

print("Audio played successfully")
