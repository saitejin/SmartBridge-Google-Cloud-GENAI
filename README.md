Gemini Historical Artifact Description App
Project Overview

The Gemini Historical Artifact Description App is a web application developed using Python and Streamlit that generates detailed descriptions of historical artifacts using Google Gemini Generative AI.

Users can enter the name of a historical artifact and optionally upload an image. The system processes the input and generates an informative and structured historical description.

This project was developed as part of the SmartBridge Virtual Internship Program.

Features

Enter artifact name

Upload artifact image (optional)

Generate historical descriptions using AI

Simple and user-friendly interface

Secure API key handling using environment variables

Technology Stack

Programming Language

Python

Libraries

Streamlit

Google GenAI

Python-dotenv

Pillow

Tools

Visual Studio Code

Git & GitHub

Installation and Setup
Clone the repository
git clone https://github.com/saitejin/SmartBridge-Google-Cloud-GENAI.git
cd GeminiArtifactApp

Create virtual environment
python -m venv venv
venv\Scripts\activate

Install dependencies
pip install -r requirements.txt

Create .env file

Create a file named .env and add:

GOOGLE_API_KEY=your_api_key_here

Run the application
streamlit run app.py

Output

The application generates historical descriptions based on user input and displays results in a web interface.

Demo Video

https://drive.google.com/drive/folders/1T9egsqeoD1bU0OEaquw_Cu_EAXHN4rYb

Team Details

Team ID: LTVIP2026TMIDS59887
Team Size: 5

Team Leader:
Nalajala Sai Teja

Team Members:

Madhu Nidrabingi

Chinta Ravi Teja

Bhargava Adithya Jidugu

Bajjuri Venkatesh

Advantages

Easy to use

Fast generation

Demonstrates AI integration

Limitations

Requires internet connection

API quota limitations may affect output

Future Enhancements

Download generated descriptions

Improve UI design

Deploy application online

Multi-language support

References

Google Gemini API

Streamlit Documentation

Python Documentation
