# pip install azure-cognitiveservices-speech

import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech import AudioDataStream, SpeechConfig, SpeechSynthesizer, SpeechSynthesisOutputFormat
from azure.cognitiveservices.speech.audio import AudioOutputConfig

speech_config = SpeechConfig(subscription="key", region="eastus")
#speech_config.speech_synthesis_voice_name="en-US-AriaNeural"
#speech_config.speech_synthesis_voice_name="en-GB-MiaNeural"
#speech_config.speech_synthesis_voice_name="en-GB-RyanNeural"
#speech_config.speech_synthesis_voice_name="en-US-JennyNeural"
#speech_config.speech_synthesis_voice_name="en-US-GuyNeural"
#speech_config.speech_synthesis_voice_name="en-IN-NeerjaNeural"
#speech_config.speech_synthesis_voice_name="en-IN-PrabhatNeural"
speech_config.speech_synthesis_voice_name="en-CA-ClaraNeural"
#speech_config.speech_synthesis_voice_name="en-CA-LiamNeural"

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

print("Type some text that you want to speak...")
text = input("Enter text : ")
#text="The Azure cloud platform is more than 200 products and cloud services designed to help you bring new solutions to life—to solve today’s challenges and create the future. Build, run and manage applications across multiple clouds, on-premises and at the edge, with the tools and frameworks of your choice."

#file=open("java.txt","r")
#text=file.read()

result = speech_synthesizer.speak_text_async(text).get()


