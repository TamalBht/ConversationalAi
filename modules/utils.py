import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏱️ {func.__name__} executed in {end-start:.2f}s")
        return result
    return wrapper

def clean_text(text):
    """Remove special characters that might cause TTS issues"""
    return ''.join(char for char in text if char.isalnum() or char in " .,!?-;:'")