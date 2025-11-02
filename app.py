from flask import Flask, render_template, request, redirect, url_for, flash
from telethon import TelegramClient
import os

app = Flask(__name__)
app.secret_key = "shati_secret_key"

BOT_TOKEN = os.environ.get("BOT_TOKEN")

api_id = 1234567
api_hash = 'your_api_hash'
client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=BOT_TOKEN)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/send_message', methods=['POST'])
def send_message():
    chat_id = request.form.get('chat_id')
    message = request.form.get('message')
    if chat_id and message:
        try:
            client.send_message(int(chat_id), message)
            flash("Message sent successfully!", "success")
        except Exception as e:
            flash(f"Error: {str(e)}", "danger")
    else:
        flash("Chat ID and Message required!", "danger")
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
