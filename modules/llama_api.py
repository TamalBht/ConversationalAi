import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Initialize client once
client = None

def get_client():
    global client
    if client is None:
        client = OpenAI(
            base_url="https://api.novita.ai/v3/openai",
            api_key=os.getenv("NOVITA_API_KEY")
        )
    return client

def get_ai_response(prompt):
    try:
        # Get system prompt
        with open('assets/system_prompt.txt', 'r') as f:
            system_prompt = f.read().strip()
        
        # Format messages
        messages = [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
        
        # Get response
        client = get_client()
        chat_completion_res = client.chat.completions.create(
            model="meta-llama/llama-3.1-8b-instruct",
            messages=messages,
            max_tokens=256,
            temperature=0.7,
            top_p=0.9,
            stream=False  # Disable streaming for simplicity
        )
        
        return chat_completion_res.choices[0].message.content.strip()
    
    except Exception as e:
        return f"Sorry, I encountered an error: {str(e)}"