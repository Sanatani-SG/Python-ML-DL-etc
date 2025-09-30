import pyttsx3 as p
import speech_recognition as sr
import webbrowser as wb
import Library as L
import requests
import google.generativeai as ai
import pyaudio 
def AI(c):
    ai.configure(api_key="AIzaSyCjdXnx8F9UXN0hw0obDd_7_xg-M8j1e5o")
    model = ai.GenerativeModel("gemini-1.5-pro-latest")
    response = model.generate_content(c)
    return response.text
R=sr.Recognizer()
Greet=p.init()
Greet.setProperty('rate',150)
V=Greet.getProperty('voices')
Greet.setProperty('voice',V[1].id)
def Speak(txt):
    Greet.say(txt)
    Greet.runAndWait()
with sr.Microphone() as S:
    R.adjust_for_ambient_noise(S)
    print("Say Chakra to interact")
    In=R.listen(S)
try:
    Txt = R.recognize_google(In).lower()
    print(Txt)
    if 'chakra' in Txt:
        Speak("Jai Shri Shyam")
        Speak("I am Chakra")
        while True:
            print("Say Something")
            with sr.Microphone() as Source:
                R.adjust_for_ambient_noise(Source)
                Input = R.listen(Source)
            Text=R.recognize_google(Input).lower()
            print(Text)
            if 'youtube' in Text:
                Speak("Opening Youtube")
                wb.open('https://www.youtube.com')
            elif 'google' in Text:
                Speak("Opening Google")
                wb.open('https://www.google.com')
            elif 'play' in Text:
                words=Text.split(' ')
                if len(words)>1:
                    s = words[1]
                    l = L.Lib.get(s)
                    if l:
                        Speak(f"Playing {s}")
                        wb.open(l)
                    else:
                        Speak(f"Sorry, I couldn't find {s}")
                else:
                    Speak("Please specify what to play")
            elif 'chakra' in Text:
                Speak("Jai Shri Shyam")
                Speak("Ask your Query")
            elif 'news' in Text:
                r=requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=7023fd54d9cf4f5cb06ebf4da79fe97a')
                if r.status_code==200:
                    data=r.json()
                    articles=data.get('articles',[])
                    for article in articles:
                        Speak(article['title'])
            elif 'exit' in Text:
                Speak("Exiting Chakra")
                break
            else:
                # output=AI(Text)
                # with open('output.txt', 'w', encoding='utf-8') as f:
                # f.write(output)

                print(output)
                Speak(output)
                
except:
    Speak("I didn't Understood what you said")



