# import streamlit as st
# from google import genai
# from google.genai import types
# from PIL import Image
# import wave

# st.markdown(
# """
# <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
# """,
# unsafe_allow_html=True
# )

# #AIzaSyDZ8mJuhil_RmgZVMClETMSqGHyVa5tczY

# with st.sidebar:
#     st.subheader("gemini api key")
#     st.text_input("Enter api key",key="api_key",type="password")
#     st.markdown("---")
#     st.subheader("👤 Connect with me")

#     st.markdown(
#             """
#         <div style="display:flex; justify-content:center; gap:20px; margin-top:10px;">
#         <a href="https://www.linkedin.com/in/YOUR-LINKEDIN-USERNAME/" target="_blank">
#         <i class="fab fa-linkedin" style="font-size:34px; color:#0A66C2;"></i>
#         </a>

#         <a href="https://github.com/YOUR-GITHUB-USERNAME" target="_blank">
#         <i class="fab fa-github" style="font-size:34px; color:black;"></i>
#         </a>
#         </div>

#         <p style="text-align:center; font-size:12px; margin-top:8px;">
#         Made by Parth Adsul
#         </p>
#             """,
#     unsafe_allow_html=True
#     )
   
       


# api_key=st.session_state.get("api_key","")

# if not api_key: #֎ AIVA
#     st.warning("please enter ur api key")
#     st.stop()

# client = genai.Client(api_key=api_key)

# st.set_page_config("AI Assistant", layout="wide")
# st.title("֎ AIVA")


# tabs = st.tabs(["💭Chat  ","🧠Systeam Mode  ","🖼️Image Analyser  ","🎙️Text to speech  ", "Image generation"])
# #for audio related
# def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
#    with wave.open(filename, "wb") as wf:
#       wf.setnchannels(channels)
#       wf.setsampwidth(sample_width)
#       wf.setframerate(rate)
#       wf.writeframes(pcm)


# with tabs[0]:
#     st.subheader("🤖 YOUR VIRTUAL ASSISTANT")
#     if "chat_history" not in st.session_state:
#         st.session_state["chat_history"]=[]

#     user_input = st.chat_input("Ask ur question")
#     if user_input:
#         st.session_state["chat_history"].append({
#             "role": "user",
#             "parts": [{"text": user_input}]
#         })
#         response = client.models.generate_content(
#         model="gemini-2.5-flash",
#         contents=st.session_state["chat_history"],
#         )
#         st.session_state["chat_history"].append({
#             "role": "model",
#             "parts": [{"text": response.text}]
#         })

#         for msg in st.session_state["chat_history"]:
#             with st.chat_message("user" if msg["role"] == "user" else "assistant"):
#                  st.write(msg["parts"][0]["text"])

            
#     car=st.button("🧹CLEAR CHAT!") 
#     if car:
#         st.session_state["chat_history"]=[]
#         st.rerun()

# with tabs[1]:
#     st.subheader("🧠Systeam Mode")
#     st.caption("Assistant response as a 15 year experienced software engineer")   
   
    
#     if "systeam_chat_history" not in st.session_state:
#         st.session_state["systeam_chat_history"]=[]
#     ######
#     syst_input=st.text_area("ask ur question")
   
#     if syst_input and st.button("🧠Run Systeam Mode"):
#         st.session_state["systeam_chat_history"].append(("user",syst_input))
#         response = client.models.generate_content(
#             model="gemini-2.5-flash",
#             config=types.GenerateContentConfig(
#                 system_instruction="You are a softwar engineer with 15 years of experience iin software field"),
#             contents=st.session_state["systeam_chat_history"]
#         )

#         st.session_state["systeam_chat_history"].append(("assistant",response.text))

#         for role,response in st.session_state["systeam_chat_history"]:
#             with st.chat_message(role):
#                 st.write(response)
            
  
#     if st.button("🧹clear systeam chat"):
#         st.session_state["systeam_chat_history"]=[]
#         st.rerun()
#     ######

# with tabs[2]:
#     st.subheader("🖼️Image Analyser")    
#     uploaded_img = st.file_uploader("Upload Image",type=["png","jpeg","jpg"])
#     if uploaded_img:
#         img = Image.open(uploaded_img)
#         response = client.models.generate_content(
#             model="gemini-2.5-flash",
#             contents=[img, "Tell me about this Image"]
#         )
#         st.success(response.text)

# with tabs[3]:
#     st.subheader("🎙️Text to speech")    
#     var=st.text_area("enter text")
#     if var and st.button("🗣️Generate speech"):
#             response = client.models.generate_content(
#                 model="gemini-2.5-flash-preview-tts",
#                 contents=f"Say cheerfully: {var}",
#                 config=types.GenerateContentConfig(
#                     response_modalities=["AUDIO"],
#                     speech_config=types.SpeechConfig(
#                         voice_config=types.VoiceConfig(
#                             prebuilt_voice_config=types.PrebuiltVoiceConfig(
#                             voice_name='Kore',
#                             )
#                         )
#                     ),
#                 )
#             )

#             data = response.candidates[0].content.parts[0].inline_data.data

#             file_name='out.wav'
#             wave_file(file_name, data) 
#             st.audio(file_name)
           

# with tabs[4]:
 

#     st.subheader("🖼️ Image Generation")
#     st.write("Powered by nano banana 🍌")
#     st.warning("Sorry this feature isn't available for free versions")
#     # prompt = st.text_area("Enter image description", key="image_prompt")

#     # if st.button("🎨 Generate Image", key="generate_image_btn") and prompt:

#     #     with st.spinner("Generating image..."):
#     #         response = client.models.generate_content(
#     #             model="gemini-2.5-flash-image",
#     #             contents=[prompt],
#     #         )

#     #         for part in response.parts:
#     #             if part.inline_data is not None:
#     #                 image = part.as_image()

#     #                 # ✅ Show image on screen
#     #                 st.image(image, caption="Generated Image", use_container_width=True)

#     #                 # ✅ Save image to memory (not just disk)
#     #                 img_bytes = io.BytesIO()
#     #                 image.save(img_bytes, format="PNG")
#     #                 img_bytes.seek(0)

#     #                 # ✅ Download button
#     #                 st.download_button(
#     #                     label="⬇️ Download Image",
#     #                     data=img_bytes,
#     #                     file_name="generated_image.png",
#     #                     mime="image/png"
#     #                 )

#     #             elif part.text is not None:
#     #                 st.info(part.text)
import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
import wave

# ================== PAGE CONFIG ==================
st.set_page_config("AI Assistant", layout="wide")

# ================== ICONS ==================
st.markdown(
"""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
""",
unsafe_allow_html=True
)

# ================== SIDEBAR ==================
with st.sidebar:
    st.subheader("🔑 Gemini API Key")
    st.text_input("Enter your API key", key="api_key", type="password")
    st.caption("Your key is not stored anywhere")

    st.markdown("---")
    st.subheader("👤 Connect with me")

    st.markdown(
        """
        <div style="display:flex; justify-content:center; gap:20px; margin-top:10px;">
            <a href="https://www.linkedin.com/" target="_blank">
                <i class="fab fa-linkedin" style="font-size:34px; color:#0A66C2;"></i>
            </a>
            <a href="https://github.com/" target="_blank">
                <i class="fab fa-github" style="font-size:34px; color:black;"></i>
            </a>
        </div>

        <p style="text-align:center; font-size:12px; margin-top:8px;">
            Made by Parth Adsul
        </p>
        """,
        unsafe_allow_html=True
    )

# ================== API KEY CHECK ==================
api_key = st.session_state.get("api_key", "")

if not api_key:
    st.warning("⚠️ Please enter your Gemini API key")
    st.stop()

client = genai.Client(api_key=api_key)

# ================== TITLE ==================
st.title("֎ AIVA")

tabs = st.tabs([
    "💭 Chat",
    "🧠 System Mode",
    "🖼️ Image Analyser",
    "🎙️ Text to Speech",
    "🎨 Image Generation"
])

# ================== AUDIO HELPER ==================
def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm)

# ==================================================
# 💭 CHAT TAB
# ==================================================
with tabs[0]:
    st.subheader("🤖 Your Virtual Assistant")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.chat_input("Ask your question")

    if user_input:
        # USER MESSAGE
        st.session_state.chat_history.append({
            "role": "user",
            "parts": [{"text": user_input}]
        })

        # GEMINI RESPONSE
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=st.session_state.chat_history
        )

        st.session_state.chat_history.append({
            "role": "model",
            "parts": [{"text": response.text}]
        })

    # DISPLAY CHAT
    for msg in st.session_state.chat_history:
        role = "user" if msg["role"] == "user" else "assistant"
        with st.chat_message(role):
            st.write(msg["parts"][0]["text"])

    if st.button("🧹 Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()

# ==================================================
# 🧠 SYSTEM MODE TAB
# ==================================================
with tabs[1]:
    st.subheader("🧠 System Mode")
    st.caption("Assistant responds as a 15-year experienced software engineer")

    if "system_history" not in st.session_state:
        st.session_state.system_history = []

    sys_input = st.text_area("Ask your question")

    if st.button("🧠 Run System Mode") and sys_input:
        st.session_state.system_history.append({
            "role": "user",
            "parts": [{"text": sys_input}]
        })

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction="You are a software engineer with 15 years of experience."
            ),
            contents=st.session_state.system_history
        )

        st.session_state.system_history.append({
            "role": "model",
            "parts": [{"text": response.text}]
        })

    for msg in st.session_state.system_history:
        role = "user" if msg["role"] == "user" else "assistant"
        with st.chat_message(role):
            st.write(msg["parts"][0]["text"])

    if st.button("🧹 Clear System Chat"):
        st.session_state.system_history = []
        st.rerun()

# ==================================================
# 🖼️ IMAGE ANALYSER TAB
# ==================================================
with tabs[2]:
    st.subheader("🖼️ Image Analyser")

    uploaded_img = st.file_uploader("Upload image", type=["png", "jpg", "jpeg"])

    if uploaded_img:
        img = Image.open(uploaded_img)

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[img, "Describe this image"]
        )

        st.image(img, use_container_width=True)
        st.success(response.text)

# ==================================================
# 🎙️ TEXT TO SPEECH TAB
# ==================================================
with tabs[3]:
    st.subheader("🎙️ Text to Speech")
    st.warning("Text-to-Speech is not available in the free Gemini API")

# ==================================================
# 🎨 IMAGE GENERATION TAB
# ==================================================
with tabs[4]:
    st.subheader("🎨 Image Generation")
    st.write("Powered by nano banana 🍌")
    st.warning("Image generation is not available in the free version")
