# 🎂 Birthday Wish Maker

HTML + CSS + Python (Flask) ka simple web app — naam daalo aur personalised birthday wish pao.

## Files
| File | Kaam |
|------|------|
| `app.py` | Flask server + birthday wish generator (Python) |
| `index.html` | Page structure + naam input form (HTML) |
| `style.css` | Birthday theme, balloons, confetti (CSS) |
| `requirements.txt` | Dependencies (`flask`) |

## Local run (apne computer par)
```bash
pip install flask
py app.py
```
Browser me kholo: **http://127.0.0.1:8000**

## Deploy to PythonAnywhere (free)
1. **GitHub** par ye code push karo (naya repo banao, phir):
   ```bash
   git remote add origin https://github.com/<your-username>/birthday-wish.git
   git push -u origin main
   ```
2. **PythonAnywhere.com** par account banao (free) → **Web** tab → **Add a new web app** → **Manual configuration** → koi bhi Python version.
3. **Bash console** kholo aur repo clone karo:
   ```bash
   git clone https://github.com/<your-username>/birthday-wish.git
   ```
4. **Web** tab me apne web app ke **WSGI file** ka link kholo (blue link — `/var/www/..._wsgi.py`) aur content ko isse replace karo:
   ```python
   import sys
   path = '/home/<your-pythonanywhere-username>/birthday-wish'
   if path not in sys.path:
       sys.path.append(path)

   from app import app as application
   ```
   (`<your-pythonanywhere-username>` aur folder name apna lagaao)
5. **Web** tab me **Reload** button dabao.
6. Apna public URL kholo (e.g. `https://<your-username>.pythonanywhere.com`) 🎉

> Note: PythonAnywhere par Flask already pre-installed hai, isliye `requirements.txt` optional hai — par repo me rakhna best practice hai.
