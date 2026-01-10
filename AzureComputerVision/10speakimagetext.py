from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech import AudioDataStream, SpeechConfig, SpeechSynthesizer, SpeechSynthesisOutputFormat
from azure.cognitiveservices.speech.audio import AudioOutputConfig

from array import array
import os
from PIL import Image
import sys
import time


subscription_key="apikey"
endpoint = "https://sohamvision.cognitiveservices.azure.com/"

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))


speech_config = SpeechConfig(subscription="speech_apikey", region="eastus")
speech_config.speech_synthesis_voice_name="en-US-AriaNeural"

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

'''
OCR: Read File using the Read API, extract text - remote
This example will extract text in an image, then print results, line by line.
This API call can also extract handwriting style text (not shown).
'''
print("===== Read File - remote =====")
# Get an image with text
#read_image_url = "https://raw.githubusercontent.com/MicrosoftDocs/azure-docs/master/articles/cognitive-services/Computer-vision/Images/readsample.jpg"
#read_image_url="https://github.com/sohamglobal/azurecognitive/blob/main/chelsea.jpeg?raw=true"
read_image_url="https://github.com/sohamglobal/azurecognitive/blob/main/music.jpeg?raw=true"
#read_image_url="https://github.com/sohamglobal/pythonai/blob/main/thanks.jpeg?raw=true"
# Call API with URL and raw response (allows you to get the operation location)
read_response = computervision_client.read(read_image_url,  raw=True)
#print(read_response)


# Get the operation location (URL with an ID at the end) from the response
read_operation_location = read_response.headers["Operation-Location"]
# Grab the ID from the URL
operation_id = read_operation_location.split("/")[-1]

# Call the "GET" API and wait for it to retrieve the results 
while True:
    read_result = computervision_client.get_read_result(operation_id)
    if read_result.status not in ['notStarted', 'running']:
        break
    time.sleep(1)

# Print the detected text, line by line
if read_result.status == OperationStatusCodes.succeeded:
    for text_result in read_result.analyze_result.read_results:
        for line in text_result.lines:
            print(line.text)
            print(line.bounding_box)

            result = speech_synthesizer.speak_text_async(line.text).get()

print()
