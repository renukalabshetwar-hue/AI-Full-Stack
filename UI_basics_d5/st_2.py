import streamlit as st 

st.set_page_config(page_title="Text Input Demo",page_icon= ".")
st.title("Text Input Demo")

st.markdown(""" 
<style>
.stApp{
background-color : #5D100A
}
<style>
""", unsafe_allow_html=True)


name = st.text_input("Enter your name:",placeholder="e.g. shanti")
st.write(f"Hi,{name}!")

secret = st.text_input("Enter your password:",type="password")
st.write(f"You entered {len(secret)} characterrs.")

comments = st.text_area("Enter additional comments:",height =150)
st.write(f"you entered {len(comments)} characters")

if st.button("submit"):
    st.write("you clicked me!")

if st.checkbox("Show Additional msg?"):
    st.write("This is the additional message. Have a good day!")



