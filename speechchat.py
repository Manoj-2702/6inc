from google.cloud import speech
import io
from deep_translator import GoogleTranslator
from google.oauth2 import service_account
import requests


# from elevenlabs import set_api_key
# set_api_key("9570efc007662076dde886058d3b6815")


client_file='inc2-389702-10f84cf342ba.json'
credentials=service_account.Credentials.from_service_account_file(client_file)
client=speech.SpeechClient(credentials=credentials)


gcs_uri='gs://6incspeech/Ram Siya Ram (Hindi) Adipurush  Prabhas  Sachet-Parampara, Manoj Muntashir S  Om Raut  Bhushan K.mp3'
config = speech.RecognitionConfig(
        # encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        enable_automatic_punctuation=True,
        sample_rate_hertz=48000,
        language_code="hi-IN",
        # use_enhanced=True,
        model='default',
    )

audio = speech.RecognitionAudio(uri=gcs_uri)

operation = client.long_running_recognize(config=config, audio=audio)

print("Waiting for operation to complete...")
response = operation.result(timeout=1000)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
for result in response.results:
    manoj=GoogleTranslator(source='auto', target='en').translate(result.alternatives[0].transcript) 
    print(manoj)
        # The first alternative is the most likely one for this portion.
    # print(f"Transcript: {result.alternatives[0].transcript}")
#     resultfinal=" ".join(line.strip() for line in manoj.splitlines())
# print(resultfinal)