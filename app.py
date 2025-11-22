import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Streamlit UI
st.set_page_config(page_title="Gemini Chat", page_icon="💬")
st.title("Ask me any Question")

# Optional: List available models (for debugging)
# models = genai.list_models()
# st.write("Available Models:", [model.name for model in models])

# User input
user_input = st.text_input("Enter your question or prompt:")

if st.button("Submit"):
    if user_input.strip() == "":
        st.warning("Please enter a prompt first.")
    else:
        with st.spinner("Generating response..."):
            try:
                model = genai.GenerativeModel("models/gemini-2.5-pro")
                response = model.generate_content([{"role": "user", "parts": [user_input]}])
                st.success("Response:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")