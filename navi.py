import speech_recognition as sr
import pyttsx3
import openai

OPENAI_KEY = "YOUR API KEY"
openai.api_key = OPENAI_KEY


def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

r = sr.Recognizer()

def record_text():
    while(1):
        try:
            with sr.Microphone() as source2:

                r.adjust_for_ambient_noise(source2, duration=0.5)

                print("I'm listening")

                #Listen to the user's input
                audio2 = r.listen(source2)

                #using google to recognise user's input
                MyText = r.recognize_google(audio2)

                return MyText
            
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("Unknown error occured")

def send_to_chatGPT(messages, model = "gpt-3.5-turbo"):

    response = openai.ChatCompletion.create(
        model = model,
        messages = messages,
        max_tokens = 150,
        n = 1,
        stop = None,
        temperature = 0.5,
    )

    message = response.choices[0].message.content
    messages.append(response.choices[0].messages)
    return message

messages = [{"role": "user", "content": "INPUT WHAT TOU WANT Chat GPT to be when the program runs"}]
while(1):
    text = record_text()
    messages.append({"role": "user", "content": text})
    response = send_to_chatGPT(messages)
    SpeakText(response)

    print(response)
