
import azure.cognitiveservices.speech as speechsdk

def from_mic():
    try:
        speech_config = speechsdk.SpeechConfig(subscription="key", region="eastus")
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    
        print("Speak into your microphone.")
        result = speech_recognizer.recognize_once_async().get()
        print(result.text)

        file=open("myspeech.txt","a")
        file.write(result.text+"\n")
    except Exception as ex:
        print(ex)

from_mic()