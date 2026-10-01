import streamlit as st 
import time

st.set_page_config(page_title="Text Input Demo",page_icon= ".")
st.title("Chat UI Demo")

# st.markdown(""" 
# <style>
# .stApp{
# background-color : #5D100A
# }
# <style>
# """, unsafe_allow_html=True)


with st.chat_message("assistant"):
    st.write(f"Hello, my name is Alexa! Type something to get started.")

user_message = st.chat_input("Type something...") 
if user_message:
    with st.chat_message("user"):
        st.write(user_message)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            time.sleep(1.5)
        st.write(f"You said {user_message}. But, i'm still in development. I can't reply yet.")   
