import os
from google import genai
from colorama import init, Fore, Style

from bot_1 import slow_print

init()
# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key="AIzaSyDcTvZ59ZIrMGQNMksv_KZ7UeHOJejybGQ")
user = input("Please enter a question to ask or type exit")
conversation_history = "\nuser : " + user
while True:    
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents="Reply in 1 line" + conversation_history
    )
    slow_print(response.text, 2)

    conversation_history = conversation_history + "\nbot :" + response.text    
    print(f"{Fore.GREEN} {conversation_history} {Style.RESET_ALL}")
    if user == "exit":
        break
    else:
        user = input("Please enter a question to ask or type exit")
        conversation_history = conversation_history + "\nuser : " + user
        
        
