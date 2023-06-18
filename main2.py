import openai
import speech_recognition as sr
import pyttsx3
from rich import print

openai.api_key = "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"


# Initialize text-to-speech engine
engine = pyttsx3.init()

voices = engine.getProperty('voices')
# Use the index that corresponds to the Hindi voice
engine.setProperty('voice', voices[1].id)
engine.setProperty('language', 'hi')

# Create speech recognizer object
r = sr.Recognizer()

# Listen for input
with sr.Microphone() as source:
    print("Speak now:")
    audio = r.listen(source)

    try:
        prompt = r.recognize_google(audio, language="hi-IN", show_all=False)
        print("You asked:", prompt)
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=300
        )
        response_text = str(response['choices'][0]['text']).strip('\n\n')
        print(response_text)

        # Speak the response
        engine.say(response_text)
        engine.runAndWait()
        print()

    except:
        response_text = "Sorry, I didn't get that!"
        print(response_text)
        engine.say(response_text)
        engine.runAndWait()
        print()
