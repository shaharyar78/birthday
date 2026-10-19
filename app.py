"""
Birthday Wish Web App — HTML + CSS + Python (Flask)

Local run:      py app.py          ->  http://127.0.0.1:8000
Deploy (WSGI):  PythonAnywhere uses:  from app import app as application
"""
import html
import os
import random

from flask import Flask, request

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
application = app  # WSGI entry point (PythonAnywhere convention)

# Each note is written to feel like a real message someone would send to a loved one.
WISHES = [
    "I hope today gives you a hundred little reasons to smile: your favourite people close by, something delicious to eat, and that lovely feeling of being celebrated. You bring so much kindness and light into other people's lives. May the year ahead bring that same warmth back to you, along with new adventures, peaceful days, and dreams that finally find their way to you.",
    "Happy birthday to someone who makes ordinary days brighter just by being in them. I hope you get time for all the things that make you happiest, a few beautiful surprises, and more cake than anyone can reasonably justify. May this next trip around the sun bring you confidence for the big plans, calm for the hard days, and people who remind you how loved you are.",
    "Today is a good excuse to say what should be said more often: you matter, you are appreciated, and the world is better with you in it. I hope your birthday feels easy and joyful, with your favourite faces around you and a wish worth making when you blow out the candles. May this new chapter be generous with laughter, good health, wonderful memories, and chances to do what you love.",
    "I hope your birthday is not just one happy day, but the start of a whole year that feels more like you: full of things you love, people who understand you, and moments you will want to remember. Keep being your thoughtful, funny, wonderful self. You deserve good news, deep rest, brave new beginnings, and all the love you give so freely to everyone around you.",
    "Wishing you a birthday filled with the kind of happiness that stays with you long after the candles are gone. May there be loud laughs, warm hugs, your favourite food, and at least one surprise that makes you say, ‘I didn't expect that!’ Thank you for being such a special person. I hope the year ahead brings you closer to everything your heart has been hoping for.",
    "Another year of you is absolutely something to celebrate. I hope today reminds you of all the people cheering for you and all the good things still waiting around the corner. May you find joy in the little moments, courage for the big ones, and plenty of reasons to feel proud of how far you've come. Have the happiest birthday—you deserve to feel loved every minute of it.",
    "May your birthday be soft where you need rest, bright where you need hope, and wonderfully silly whenever life gives you the chance. I hope the people you love make a fuss over you, your cake is excellent, and your next year brings more yeses, more adventures, and more days that end with a grateful heart. Sending you the biggest birthday hug and so much love.",
    "Happy birthday! I hope this next chapter surprises you in the best ways: with new places to explore, new things to be proud of, and old friends who keep showing up. You have a way of making people feel welcome and cared for; I hope today you get to feel all of that love returned. Make a wish, take the extra slice, and let yourself be celebrated.",
]


def make_wish_card(name, relationship, special_thing, memory):
    """Generate the personalized birthday wish HTML card."""
    safe_name = html.escape(name)
    relationship_names = {
        "friend": "friend",
        "sibling": "sibling",
        "parent": "parent",
        "partner": "favorite person",
        "coworker": "wonderful teammate",
        "family": "family member",
    }
    recipient_role = relationship_names.get(relationship, "someone special")
    safe_special_thing = html.escape(special_thing)
    safe_memory = html.escape(memory)
    wish = random.choice(WISHES)
    personal_lines = []
    if safe_special_thing:
        personal_lines.append(
            f"One of my favourite things about you is {safe_special_thing}. "
            "It makes being around you feel like a gift."
        )
    if safe_memory:
        personal_lines.append(
            f"I still smile when I think about {safe_memory}. "
            "I hope we make many more memories just like it this year."
        )
    personal_html = "".join(f"<p>{line}</p>" for line in personal_lines)
    return f"""
    <section class="wish-card" id="birthday-wish" aria-labelledby="wish-title">
      <div class="wish-card-topline"><span class="wish-kicker">A note made just for you</span><span aria-hidden="true">✦ ✦ ✦</span></div>
      <div class="wish-card-art" aria-hidden="true"><span class="wish-sun">✹</span><span class="wish-cake">🎂</span><span class="wish-heart">♡</span></div>
      <p class="wish-overline">TODAY, WE CELEBRATE OUR {html.escape(recipient_role.upper())}</p>
      <h2 class="wish-title" id="wish-title">Happy Birthday, {safe_name}!</h2>
      <div class="wish-text" id="wish-message"><p>{wish}</p>{personal_html}</div>
      <div class="wish-signoff"><span class="signoff-line"></span><span>With all my love</span><span class="signoff-heart">♥</span><span class="signoff-line"></span></div>
      <div class="wish-actions"><button class="wish-action copy-button" type="button" data-copy-target="wish-message"><span aria-hidden="true">▢</span> Copy this wish</button><button class="wish-action share-button" type="button"><span aria-hidden="true">↗</span> Share the love</button></div>
      <p class="wish-try">A little reminder: you make the world brighter just by being in it.</p>
    </section>
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
    name = (request.form.get("name") or "").strip()[:40]
    if not name:
        name = "Dear Friend"
    relationship = (request.form.get("relationship") or "friend").strip().lower()
    special_thing = (request.form.get("special_thing") or "").strip()[:90]
    memory = (request.form.get("memory") or "").strip()[:140]
    return render_page(make_wish_card(name, relationship, special_thing, memory))


if __name__ == "__main__":
    # Render provides PORT at runtime; localhost is used for local development.
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8000")))
