import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser


engine = pyttsx3.init()

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def get_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
        except sr.RequestError:
            speak("Sorry, the speech service is down.")
    return ""

def process_command(command):
    if "hello" in command or "hi" in command:
        speak("Hello! How can I help you?")
    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {now}")
    elif "date" in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")
    elif "search" in command:
        speak("What do you want to search for?")
        query = get_command()
        if query:
            speak(f"Searching for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")
    elif "exit" in command or "bye" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I can't do that yet.")

if __name__ == "__main__":
    speak("Hi, I am your voice assistant!")

    while True:
        command = get_command()
        if command:
            process_command(command)
