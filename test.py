import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("AIzaSyAyEQjRUVdi_XlwSaoI-NbwIdFy4MVr8Yw"))

response = client.models.generate_content(
    model="gemini-1.5-flash",
    contents="Explain pyramids in 50 words"
)

print(response.text)