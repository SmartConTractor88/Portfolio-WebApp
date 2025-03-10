import streamlit as st

st.header("Contact Me")

with st.form(key="e-mail"):
    user_email = st.text_input("Enter your email")
    message = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    if button:
        print("YES")