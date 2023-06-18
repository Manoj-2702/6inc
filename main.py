import speech_recognition as sr
import os
import win32com.client
import openai

speaker = win32com.client.Dispatch("SAPI.SpVoice")


def say(text):
    # print("What do you want the computer to speak")
    speaker.Speak(text)


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-IN')
            print(f"User said:{query}")
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=query,
                temperature=0.7,
                max_tokens=300
            )
            response_text = str(response['choices'][0]['text']).strip('\n\n')
            print(response_text)
        except Exception as e:
            return "Some error Occurred..Sorry "
        return query


if __name__ == '__main__':
    print("Manoj")
    while True:
        print("Listening....")
        text = take_command()
        say(text)
