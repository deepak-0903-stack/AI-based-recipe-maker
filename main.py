import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
client=genai.Client(api_key=os.getenv("API_KEY")) or st.secrets.get("API_KEY")
st.title("Recipe Generator")
ingredients=st.text_input("Enter Ingredients:")
if st.button("Generate"):
    if ingredients:
        resp=client.models.generate_content(model="gemini-2.0-flash" , contents=f"Generate a recipe with {ingredients} as ingredients.")
        st.markdown(resp.text)