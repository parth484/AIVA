import os
from google import genai
from google.genai import types
from PIL import Image
import wave

# ------------------ CONFIG ------------------
API_KEY = "AIzaSyDcTvZ59ZIrMGQNMksv_KZ7UeHOJejybGQ"
client = genai.Client(api_key=API_KEY)


# ------------------ COMMON UTILS ------------------

def get_user_input(prompt="Enter text: "):
    return input(prompt)

def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm)


# ------------------ TEXT CHAT ------------------

def chat_once():
    user = get_user_input("Ask Gemini (or type exit): ")
    if user.lower() == "exit":
        print("Bye!")
        return

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user
    )
    print("Response:", response.text)


def chat_loop():
    while True:
        user = get_user_input("Ask Gemini (or type exit): ")
        if user.lower() == "exit":
            print("Exiting chat mode.")
            break
        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user
        )
        print("Response:", response.text)


# ------------------ SYSTEM INSTRUCTION MODE ------------------

def system_instruction_query():
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction="You are a software engineer with 15 years of experience in cloud"
        ),
        contents="Tell me how Entra ID authentication works in Azure"
    )
    print("System Mode Reply:")
    print(response.text)


# ------------------ IMAGE ANALYSIS ------------------

def analyze_image(image_path):
    image = Image.open(image_path)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[image, "Tell me about this Image"]
    )
    print("Image Understanding Reply:")
    print(response.text)


# ------------------ TEXT TO SPEECH ------------------

def text_to_speech(text):
    response = client.models.generate_content(
        model="gemini-2.5-flash-preview-tts",
        contents="Say in Encouraging Tone::" + text,
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Kore',
                    )
                )
            ),
        )
    )

    audio_data = response.candidates[0].content.parts[0].inline_data.data
    wave_file("out.wav", audio_data)
    print("Audio saved as out.wav")


def text_to_speech_from_input():
    user = get_user_input("Enter text to convert into speech: ")
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents="Answer in 1 line only " + user
    )
    
    reply = response.text
    print("Short Reply:", reply)
    text_to_speech(reply)


# ------------------ MENU ------------------

def main():
    print("""
1. Single chat
2. Continuous chat loop
3. System instruction example
4. Analyze image
5. Text -> speech
6. Exit
""")
    
    choice = get_user_input("Choose option: ")

    if choice == "1":
        chat_once()
    elif choice == "2":
        chat_loop()
    elif choice == "3":
        system_instruction_query()
    elif choice == "4":
        path = get_user_input("Enter image path: ")
        analyze_image(path)
    elif choice == "5":
        text_to_speech_from_input()
    else:
        print("Goodbye!")


# ------------------ RUN ------------------
main()
