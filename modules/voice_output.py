import os
import tempfile
import pygame
from gtts import gTTS
from dotenv import load_dotenv

load_dotenv()

def speak(text):
    print(f"🤖 Assistant: {text}")
    
    try:
        if not pygame.mixer.get_init():
            pygame.mixer.init()
        
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp_file:
            tts = gTTS(text=text, lang=os.getenv("LANGUAGE", "en"), slow=False)
            tts.save(tmp_file.name)
            
            pygame.mixer.music.load(tmp_file.name)
            pygame.mixer.music.play()
            
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
                
            pygame.mixer.music.unload()
            os.remove(tmp_file.name)
            
    except Exception as e:
        print(f"TTS Error: {e}")
        try:
            import pyttsx3
            engine = pyttsx3.init()
            engine.setProperty('rate', 180)
            engine.say(text)
            engine.runAndWait()
        except:
            print(f"System would say: {text}")