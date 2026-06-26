import datetime
import streamlit as st
from google import genai
from google.genai import types

st.markdown("""
            <h1 style = 'text-align: center;'> Tyagi ji ka AI Assistant </h1>
            <p style ='text-align: center; font-size:18px;'>
            Ask any Question.
            </p>
            """,
            unsafe_allow_html=True,
            )

# 1. Initialize BOTH the client and chat session inside session_state together
if "robo" not in st.session_state:
    st.session_state.robo = genai.Client(api_key=st.secrets["MY_API"])

if "myChat" not in st.session_state:
    today = datetime.date.today().strftime("%B %d, %Y")
    # Use the session_state client to build the chat
    st.session_state.myChat = st.session_state.robo.chats.create(
        model="gemini-2.5-flash", 
        config=types.GenerateContentConfig(
            system_instruction=f"You are Tyagi ji ka AI Assistant. Today's real-world date is {today}. Always use this date as your anchor for current events or relative time questions."
        )
    )

response_placeholder = st.empty()
question = st.text_input("", placeholder="Question : ")

col1, col2, col3 = st.columns([4,1,4])
with col2:
    send = st.button("Send")

if send and question:
    # 2. Call send_message using the chat attached to the persistent client
    response = st.session_state.myChat.send_message(question)
    response_placeholder.write(response.text)
