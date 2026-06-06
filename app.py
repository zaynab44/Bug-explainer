from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/explain", methods=["POST"])
def explain():
    data = request.get_json()
    bug_input = data.get("bug", "")

    if not bug_input:
        return jsonify({"error": "No input provided"}), 400

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful coding assistant. When given an error message or buggy code, do these 4 things: 1. Explain what the error means in simple words. 2. Explain why it happened. 3. Give the fixed code. 4. Explain what you changed and why. Be clear and beginner friendly."
                },
                {
                    "role": "user",
                    "content": "Here is my bug or error:\n\n" + bug_input
                }
            ]
        )
        answer = completion.choices[0].message.content
        return jsonify({"answer": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)