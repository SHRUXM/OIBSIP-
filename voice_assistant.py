import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I'm having trouble connecting to the speech service.")
        return ""
    return query

if __name__ == "__main__":
    while True:
        query = take_command().lower()

        if "hello" in query:
            speak("Hello! How can I help you today?")
        elif "time" in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {current_time}")
        elif "date" in query:
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            speak(f"Today's date is {current_date}")
        elif "search wikipedia" in query:
            query = query.replace("search wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
            except wikipedia.exceptions.PageError:
                speak(f"Sorry, I couldn't find anything about {query} on Wikipedia.")
            except wikipedia.exceptions.DisambiguationError as e:
                speak(f"There are multiple results for {query}. Could you be more specific?")
        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube...")
        elif "open google" in query:
            webbrowser.open("https://www.google.com")
            speak("Opening Google...")
        elif "exit" in query or "quit" in query:
            speak("Goodbye!")
            break
        elif "exit" in query or "quit" in query: # This is a duplicate condition
            speak("I'm sorry, I didn't understand that command.") # This will never be reached
        else:
            speak("I'm sorry, I didn't understand that command.")
