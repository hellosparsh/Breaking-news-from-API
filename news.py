# API key is: 1778bc03d3354ea4963a0262b281acac
def speak(msg):
    import pyttsx3
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 130)
    engine.say(msg)
    engine.runAndWait()
import requests
data=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=YOUR_API_KEY_HERE")
full=data.json()
news=full["articles"]
speak("Hello, here are the top 5 breaking news")
for i in range(5):
    speak(f"News number {i+1}")
    speak(news[i]["description"])
    if i==4:
        speak("Thank you for listening")