from modules.voice_input import capture_voice
from modules.llama_api import get_ai_response
from modules.voice_output import speak
from dotenv import load_dotenv
import pygame
import time
import os

# Initialize pygame once
pygame.init()

load_dotenv()

def main():
    model_name = os.getenv("MODEL_NAME", "meta-llama/llama-3.1-8b-instruct")
    print(f"🎤 Llama Voice Assistant - Ready (Using {model_name} via Novita)")
    
    while True:
        try:
            # Capture voice input
            user_input = capture_voice()
            if not user_input:
                continue
                
            # Exit condition
            if "exit" in user_input.lower() or "quit" in user_input.lower():
                speak("Goodbye!")
                break
                
            # Get AI response
            print("🔄 Processing with Llama 3.1...")
            ai_response = get_ai_response(user_input)
            
            # Convert to speech
            speak(ai_response)
            
            # Brief pause before next input
            time.sleep(0.5)
            
        except KeyboardInterrupt:
            speak("Assistant shutting down")
            break
        except Exception as e:
            print(f"Critical error: {e}")
            speak("I'm having technical difficulties. Please restart me.")
            break

if __name__ == "__main__":
    try:
        main()
    finally:
        pygame.quit()