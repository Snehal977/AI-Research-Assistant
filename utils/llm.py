import os
import streamlit as st
from google.api_core.exceptions import ResourceExhausted
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()
try:
    api_key = st.secrets[
        "GOOGLE_API_KEY"
    ]
except:
    api_key = os.getenv(
        "GOOGLE_API_KEY"
    )
genai.configure(api_key=api_key)
model=genai.GenerativeModel("gemini-2.5-flash")
#def generate_answer(prompt):
    #response=model.generate_content(prompt)
   # return response.text
def generate_answer(prompt):

    try:

        response = model.generate_content(
            prompt
        )

        return response.text

    except ResourceExhausted:

        return (
            "Gemini quota exceeded. "
            "Please wait a minute and try again."
        )
