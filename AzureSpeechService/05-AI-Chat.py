import azure.cognitiveservices.speech as speechsdk
from datetime import datetime

import platform
import os
import re

def get_system_info():
    os_name = platform.system()
    os_version = platform.release()
    architecture = platform.architecture()[0]
    processor = platform.processor()

    return f"You are using {os_name} {os_version}, {architecture}, processor {processor}"

def open_calculator():
    os.system("calc")


def extract_numbers(text):
    return list(map(int, re.findall(r'\d+', text)))

def add_numbers(numbers):
    if len(numbers) >= 2:
        return numbers[0] + numbers[1]
    return None
# ========== AZURE CONFIG ==========
SPEECH_KEY = "key"
REGION = "eastus"

speech_config = speechsdk.SpeechConfig(
    subscription=SPEECH_KEY,
    region=REGION
)

# Voice settings (optional but nice)
speech_config.speech_synthesis_voice_name = "en-IN-NeerjaNeural"

# Microphone input
audio_input = speechsdk.AudioConfig(use_default_microphone=True)

# Create recognizer & synthesizer
recognizer = speechsdk.SpeechRecognizer(
    speech_config=speech_config,
    audio_config=audio_input
)

synthesizer = speechsdk.SpeechSynthesizer(
    speech_config=speech_config
)

print("🎤 Voice assistant started...")
print("Say: date | time | hello | stop")

# ========== MAIN LOOP ==========
while True:
    print("\nListening...")
    result = recognizer.recognize_once()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        command = result.text.lower()
        print("You said:", command)

        response = ""

        if "date" in command:
            response = f"Today's date is {datetime.now().strftime('%d %B %Y')}"

        elif "time" in command:
            response = f"The current time is {datetime.now().strftime('%I:%M %p')}"

        elif "hello" in command:
            response = "Hello! How can I help you?"

        elif "thank you" in command or "thanks" in command:
            response = "You're welcome! If you have any more questions, feel free to ask."

        elif "system" in command or "os" in command or "processor" in command:
            response = get_system_info()

        elif "calculator" in command:
            open_calculator()
            response = "Opening calculator..."
        
        elif "add" in command:
            numbers = extract_numbers(command)
            if len(numbers) >= 2:
                result = add_numbers(numbers)
                response = f"The sum of {numbers[0]} and {numbers[1]} is {result}"
            else:
                response = "Please tell two numbers to add."


        elif "stop" in command:
            response = "Stopping the voice assistant. Goodbye!"
            synthesizer.speak_text(response)
            break

        else:
            response = "Sorry, I did not understand that command."

        print("Assistant:", response)
        synthesizer.speak_text(response)

    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech recognized.")

    elif result.reason == speechsdk.ResultReason.Canceled:
        print("Speech recognition canceled.")
        break

print("Assistant stopped.")
