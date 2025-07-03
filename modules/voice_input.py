import speech_recognition as sr
from dotenv import load_dotenv
import os

load_dotenv()

def capture_voice(timeout=5, phrase_time_limit=10):
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("🔊 Calibrating microphone...")
        r.adjust_for_ambient_noise(source, duration=1)
        print("🔊 Listening...")
        
        try:
            audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        except sr.WaitTimeoutError:
            print("⌛ Listening timed out")
            return ""
        except Exception as e:
            print(f"🎤 Microphone error: {e}")
            return ""
    
    try:
        text = r.recognize_google(audio)
        print(f"👤 User: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Speech not understood")
        return ""
    except sr.RequestError as e:
        print(f"❌ API Error: {e}")
        return ""