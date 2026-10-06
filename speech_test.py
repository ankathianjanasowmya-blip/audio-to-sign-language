import speech_recognition as sr

audio_file = "audio.wav"

recognizer = sr.Recognizer()

try:
    with sr.AudioFile(audio_file) as source:
        print("Reading audio...")
        audio = recognizer.record(source)

    print("Converting speech to text...")

    text = recognizer.recognize_google(audio)

    print("\nRecognized Text:")
    print(text)

except FileNotFoundError:
    print("Error: audio.wav was not found.")

except sr.UnknownValueError:
    print("Could not understand the audio.")

except sr.RequestError as e:
    print("Speech recognition service error:", e)

except Exception as e:
    print("Error:", e)