# Bug Explainer

An AI-powered web application that explains code errors in plain English and provides instant fixes. Paste any error message or buggy code and get a clear explanation of what went wrong and how to resolve it.

## Live Demo
https://bug-explainer.up.railway.app/

## Features

- Explains any error message in simple language
- Provides the corrected code with explanation
- Supports all major programming languages
- Clean dark themed interface

## Tech Stack

- Python
- Flask
- Groq API — LLaMA 3.3 70B
- HTML, CSS, JavaScript

## Getting Started

Clone the repository and navigate to the project folder.

Create a virtual environment and activate it:
python -m venv venv
venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Create a .env file and add your Groq API key:
GROQ_API_KEY=your_key_here

Run the application:
python app.py

Open in browser:
http://localhost:5000

## API Key

Get a free Groq API key at https://console.groq.com

## Author

Zainab
BS Information Technology
University of Lahore