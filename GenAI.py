import streamlit as st
from google import genai
st.markdown("""
            <h1 style = 'text-align: center;'> Tyagi ji ka AI Assistant </h1>
            <p style ='text-align: center; font-size:18px;'?
            Ask any Python Question.
            </p>
            """,
            unsafe_allow_html=True,
            )
robo = genai.Client(api_key="MY_API")
myChat=robo.chats.create(model="gemini-3.1-flash-lite")
response_placeholder = st.empty()
question = st.text_input("", placeholder= "Question : ")
col1, col2, col3 = st.columns([4,1,4])
with col2:
    send=st.button("Send")
if send:
    response=myChat.send_message(question)
    response_placeholder.write(response.text)
