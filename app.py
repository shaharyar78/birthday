"""
Birthday Wish Web App — HTML + CSS + Python (Flask)

Local run:      py app.py          ->  http://127.0.0.1:8000
Deploy (WSGI):  PythonAnywhere uses:  from app import app as application
"""
import html
import os
import random

from flask import Flask, request, send_from_directory

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
application = app  # WSGI entry point (PythonAnywhere convention)

# Personalized birthday wishes (Python picks one at random)
WISHES = [
    "May your day be filled with laughter, cake and all the happiness in the world!",
    "Wishing you a year ahead full of dreams that come true and moments that make you smile!",
    "On your special day, may every candle you blow out carry a wish that comes true!",
    "Here's to another amazing year of you — stay awesome and keep shining bright!",
    "May today be as sweet as the cake and as bright as the candles. Happy Birthday!",
    "Sending you a big birthday hug and wishes for health, love and endless joy!",
    "May your birthday be the start of a wonderful new chapter. Enjoy every moment!",
]


def make_wish_card(name):
    """Generate the personalized birthday wish HTML card."""
    safe_name = html.escape(name)
    wish = random.choice(WISHES)
    return f"""
    <div class="wish-card">
      <div class="cake" aria-hidden="true">🎂</div>
      <h2 class="wish-title">Happy Birthday, {safe_name}! 🎉</h2>
      <p class="wish-text">"{wish}"</p>
      <p class="wish-footer">With lots of love &amp; best wishes ❤️</p>
      <p class="wish-try">Want to wish someone else? Enter another name above.</p>
    </div>
    """


def render_page(wish_html=""):
    """Load index.html and inject the wish section (empty or filled)."""
    with open(os.path.join(BASE_DIR, "index.html"), "r", encoding="utf-8") as f:
        page = f.read()
    return page.replace("<!--WISH_SECTION-->", wish_html)


@app.route("/")
def index():
    return render_page()


@app.route("/wish", methods=["POST"])
def wish():
    name = (request.form.get("name") or "").strip()
    if not name:
        name = "Dear Friend"
    return render_page(make_wish_card(name))


@app.route("/style.css")
def style():
    return send_from_directory(BASE_DIR, "style.css")


if __name__ == "__main__":
    # Render provides PORT at runtime; localhost is used for local development.
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8000")))
