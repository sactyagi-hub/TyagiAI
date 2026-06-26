import datetime
import streamlit as st
from google import genai
from google.genai import types
st.markdown("""
            <h1 style = 'text-align: center;'> Tyagi ji ka AI Assistant </h1>
            <p style ='text-align: center; font-size:18px;'
            Ask any Python Question.
            </p>
            """,
            unsafe_allow_html=True,
            )
today = datetime.date.today().strftime("%B %d, %Y")
#robo = genai.Client(api_key="MY_API")
robo= genai.Client(api_key=st.secrets["MY_API"])
#myChat=robo.chats.create(model="gemini-3.1-flash-lite")
myChat = robo.chats.create(
    model="gemini-3.1-flash-lite", # Note: gemini-2.5-flash is the standard recommended model
    config=types.GenerateContentConfig(
        system_instruction=f"You are Tyagi ji ka AI Assistant. Today's real-world date is {today}. Always use this date as your anchor for current events or relative time questions."
    )
)
response_placeholder = st.empty()
question = st.text_input("", placeholder= "Question : ")
col1, col2, col3 = st.columns([4,1,4])
with col2:
    send=st.button("Send")
if send and question:
    response=myChat.send_message(question)
    response_placeholder.write(response.text)
