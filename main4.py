import speech_recognition as sr
import os
import webbrowser
import openai
from config import API_KEY
# import datetime
from gtts import gTTS
import random
import numpy as np
import win32com.client
# from translate import Translator
from google.cloud import translate
os.environ['GOOGLE_CREDENTIALS'] = r'C:\Users\HP\Desktop\Internships\Assistant\inc2-389702-7223d1f65e50.json'

speaker = win32com.client.Dispatch("SAPI.SpVoice")
chatStr = ""
# https://youtu.be/Z3ZAJoi4x6Q


def say(text):
    # print("What do you want the computer to speak")
    speaker.Speak(text)


def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = API_KEY
    chatStr += f"User: {query}\n Chatbot: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


def ai(prompt):
    openai.api_key = API_KEY
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    print(response["choices"][0]["text"])
    say(response["choices"][0]["text"])
    # chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]
    # if not os.path.exists("Openai"):
    #     os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    # with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
    #     f.write(text)


def takeCommandHI():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        # r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
        try:
            print("Recognizing...")
            # translate_client = translate.Client()
            query = r.recognize_google(audio, language='hi-IN')
            # text = openai.Audio.translate("whisper-1", query)
            # print(text)
            # client = translate.TranslationServiceClient()
            # parent = client.location_path('inc2-389702', 'global')
            # response = client.translate_text(
            #     request={
            #         "parent": parent,
            #         "contents": [query],
            #         "mime_type": "text/plain",
            #         "source_language_code": "hi",
            #         "target_language_code": "en",
            #     }
            # )
            # translation = response.translations[0].translated_text
            # print(f"Translated Text: {translation}")

            # target = 'en'
            # output = translate_client.translate(query, target_language=target)
            # translator = Translator(to_lang='en-IN')
            # # from_lang = 'en-IN'
            # # to_lang = 'hi-IN'
            # translation = translator.translate(query)
            # # text = translation.text
            # # gTTS(text=text, lang=to_lang, slow=False)
            print(f"User said: {query}")
            # print(f"User Translation said: {output}")
            return query
            # return translation
        except Exception as e:
            return f"Some Error Occurred. Sorry from chatbot {e}"


def takeCommandEN():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        # r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            # translator = Translator(to_lang='en-IN')
            # from_lang = 'en-IN'
            # to_lang = 'hi-IN'
            # translation = translator.translate(query)
            # text = translation.text
            # gTTS(text=text, lang=to_lang, slow=False)
            print(f"User said: {query}")
            # print(f"The tranlation is : {translation}")
            return query
        except Exception as e:
            return f"Some Error Occurred. Sorry from chatbot {e}"


if __name__ == '__main__':
    print('Welcome to A.I Chatbot')
    while True:
        print("Listening...")
        print("Which Language do u want to speak in ?\n1.English\n2.Hindi")
        num = int(input("Enter the number\n"))
        if num == 1:
            query = takeCommandEN()
            ai(prompt=query)
        elif num == 2:
            query = takeCommandHI()
            ai(prompt=query)
        # if "Using artificial intelligence".lower() in query.lower():

        # elif "Jarvis Quit".lower() in query.lower():
        #     exit()

        # elif "reset chat".lower() in query.lower():
        #     chatStr = ""

        # else:
        #     print("Chatting...")
        #     chat(query)

        # say(query)
