from google.cloud import speech
import io
from google.oauth2 import service_account

client_file='inc-389615-66d58ce8b86c.json'
credentials=service_account.Credentials.from_service_account_file(client_file)
client=speech.SpeechClient(credentials=credentials)


gcs_uri='gs://manojspeech2/Ram Siya Ram (Hindi) Adipurush  Prabhas  Sachet-Parampara, Manoj Muntashir S  Om Raut  Bhushan K.mp3'
config = speech.RecognitionConfig(
        # encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        enable_automatic_punctuation=True,
        sample_rate_hertz=16000,
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
        # The first alternative is the most likely one for this portion.
    print(f"Transcript: {result.alternatives[0].transcript}")
