import os
import time
import sys
from google import genai
from google.genai import types
from PIL import Image
import wave
from colorama import init, Fore, Style

# ------------------ CONFIG ------------------
API_KEY = "AIzaSyDcTvZ59ZIrMGQNMksv_KZ7UeHOJejybGQ"  # << Don't hardcode for students in real use
client = genai.Client(api_key=API_KEY)

init()  # colorama init

# ------------------ COMMON UTILS ------------------

def get_user_input(prompt="Enter text: "):
    return input(prompt)

def slow_print(text, delay=0.02):#for bot's answer
    """Print text like a chatbot typing"""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def thinking_animation():
    """Loading animation"""
    dots = ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]
    for _ in range(1):
        for d in dots:
            print(f"\r🤖 Thinking {d}", end="", flush=True)
            time.sleep(0.08)
    print("\r", end="")

# ------------------ TEXT CHAT ------------------

def chat_once(user):
    """Send one user input to Gemini"""
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user
        )
        
        return response.text
    except Exception as e:
        return f"⚠️ Error: {e}"

def start_chat():
    slow_print(Fore.CYAN + "\n✨ Welcome to Gemini CLI Chatbot ✨", 0.05)
    slow_print(Fore.YELLOW + "Type 'exit' to quit\n", 0.03)

    while True:
        user = get_user_input(Fore.GREEN + "👤 You: " + Style.RESET_ALL)

        if user.lower() == "exit":
            slow_print(Fore.MAGENTA + "👋 Goodbye! Keep learning GenAI!" + Style.RESET_ALL)
            break

        thinking_animation()
        bot_reply = chat_once(user)
        

        print(Fore.BLUE + "🤖 Bot: " + Style.RESET_ALL, end="")
        slow_print(bot_reply, 0.02)
        print()

# ------------------ MAIN ------------------

if __name__ == "__main__":
    start_chat()

