import speech_recognition as sr
import webbrowser
import pyttsx3
from music_library import music as music_library


recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Sample music library for demonstration


def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    command = command.lower()
    if "open google" in command:
        webbrowser.open("http://google.com")
    elif "open instagram" in command:
        webbrowser.open("http://instagram.com")
    elif "open youtube" in command:
        webbrowser.open("http://youtube.com")
    elif command.startswith("play"):
        parts = command.split(" ")
        if len(parts) > 1:
            song = parts[1]
            if song in music_library:
                link = music_library[song]
                webbrowser.open(link)
            else:
                speak(f"Sorry, I don't have {song} in my library.")
        else:
            speak("Please specify a song to play.")
    else:
        speak("Sorry, I didn't understand the command.")

def main():
    speak("Initializing Jarvis....")
    while True:
        print("Listening for wake word 'Jarvis'...")
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
            word = recognizer.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Yes?")
                print("Jarvis Active... Listening for command...")
                with sr.Microphone() as source:
                    audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
                    command = recognizer.recognize_google(audio)
                    print(f"Command received: {command}")
                    processCommand(command)

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
