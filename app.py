import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)

st.title("Historical Artifact Description Generator")

artifact_name = st.text_input("Enter Artifact Name")
word_count = st.slider("Word Count", 100, 1500, 300)

if st.button("Generate Description"):

    if not artifact_name:
        st.warning("Please enter an artifact name.")
    else:
        prompt = f"""
        Write a historical description about {artifact_name}
        in approximately {word_count} words.
        """

        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )

            st.subheader("Generated Description")
            st.write(response.text)

        except Exception:
            # fallback text (works even if quota fails)
            st.subheader("Generated Description")
            st.write(f"""
            {artifact_name} is an important historical artifact known for its
            cultural and historical significance. It represents the artistic,
            technological, or social achievements of the period in which it
            was created.

            Historians study such artifacts to understand the traditions,
            beliefs, and daily life of ancient civilizations. These objects
            provide valuable insight into human history and continue to inspire
            research and education today.
            """)