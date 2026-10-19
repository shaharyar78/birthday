# Birthday Wish Maker

A small Flask app that creates a personalized birthday wish from a name.

## Run locally

```bash
python -m pip install -r requirements.txt
python app.py
```

Open <http://127.0.0.1:8000>.

## Deploy on Render

1. Push this repository to GitHub or another Git provider connected to Render.
2. In Render, choose **New → Blueprint** and select this repository. Render reads
   `render.yaml` to create the web service.
3. Confirm the `birthday-wish-maker` service and deploy it. The blueprint uses
   Render's free web service plan; you can change the plan in `render.yaml` if
   needed.

The blueprint installs dependencies from `requirements.txt`, starts the app with
Gunicorn, and checks `/` for service health. No secrets or additional environment
variables are required. Render assigns the service's port automatically.

## Files

| File | Purpose |
| --- | --- |
| `app.py` | Flask routes and birthday wish generation |
| `index.html` | Page structure and name form |
| `style.css` | Page styling and animations |
| `requirements.txt` | Flask and Gunicorn dependencies |
| `render.yaml` | Render Blueprint deployment configuration |
