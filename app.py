from flask import Flask, request, render_template
import openai
app = Flask(__name__)
with open("prompt.txt", "r", encoding="utf-8") as f:
    system_prompt = f.read()

import os
openai.api_key = os.getenv("OPENAI_API_KEY")
# Load system prompt




chat_history = []

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", response=None, chat_history=chat_history)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form.get("user_input")
    if not user_input:
        return render_template("index.html", response="❌ No input", chat_history=chat_history)

    try:
        messages = [{"role": "system", "content": system_prompt}] + chat_history
        messages.append({"role": "user", "content": user_input})

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            temperature=0.7,
            max_tokens=500
        )

        assistant_reply = response.choices[0].message["content"].strip()
        chat_history.append({"role": "user", "content": user_input})
        chat_history.append({"role": "assistant", "content": assistant_reply})

        return render_template("index.html", response=assistant_reply, chat_history=chat_history)

    except Exception as e:
        return render_template("index.html", response=str(e), chat_history=chat_history)

@app.route("/clear")
def clear_chat():
    chat_history.clear()
    return render_template("index.html", response=None, chat_history=[])

if __name__ == "__main__":
    app.rund(debug=True)
