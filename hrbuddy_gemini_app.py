import streamlit as st
import google.generativeai as genai
import os

# API-sleutel ophalen uit secrets
api_key = st.secrets.get("GEMINI_API_KEY")
if not api_key:
    st.error("⚠️ Voeg je GEMINI_API_KEY toe in Streamlit secrets.")
    st.stop()

genai.configure(api_key=api_key)

st.set_page_config(page_title="HRbuddy (Gemini)", layout="centered")
st.title("🤖 HRbuddy – powered by Gemini")
st.markdown("Stel hier je HR-vraag, Gemini denkt met je mee.")

user_input = st.text_input("💬 Typ je vraag hier:")

if user_input:
    with st.spinner("Even nadenken…"):
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_input)
        st.success(response.text)
