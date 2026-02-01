import os
#os.environ['GEMINI_API_KEY'] = "AIzaSyDcTvZ59ZIrMGQNMksv_KZ7UeHOJejybGQ"

from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key="AIzaSyDcTvZ59ZIrMGQNMksv_KZ7UeHOJejybGQ")

# while True:
#     user = input("Please enter a question to ask or type exit")
#     response = client.models.generate_content(
#         model="gemini-2.5-flash", contents=user
#     )

#     print(response.text)

#     if user == "exit":
#         break
    
# from google import genai
# from google.genai import types

# response = client.models.generate_content(
#     model="gemini-2.5-flash",
#     config=types.GenerateContentConfig(
#         system_instruction="You are a software engineer with 15 years of experience in cloud "),
#     contents="Tell me how entra id authentication works in azure "
# )

# print(response.text)


# from PIL import Image
# from google import genai

# image = Image.open(r"c:\Users\SanketD\Desktop\Unicorn.png")
# response = client.models.generate_content(
#     model="gemini-2.5-flash",
#     contents=[image, "Tell me about this Image"]
# )
# print(response.text)


from google import genai
from google.genai import types
import wave

user = input("Please enter a question to ask or type exit")
response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Answer in 1 line only " + user
)

reply = response.text

print("**************Reply generate****************")
print(reply)
# Set up the wave file to save the output:
def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
   with wave.open(filename, "wb") as wf:
      wf.setnchannels(channels)
      wf.setsampwidth(sample_width)
      wf.setframerate(rate)
      wf.writeframes(pcm)



response = client.models.generate_content(
   model="gemini-2.5-flash-preview-tts",
   contents="Say in Encouraging Tone::" + reply,
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

data = response.candidates[0].content.parts[0].inline_data.data

file_name='out2.wav'
wave_file(file_name, data) # Saves the file to current directory