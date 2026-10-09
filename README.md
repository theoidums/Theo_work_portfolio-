# Flask Portfolio

A Flask conversion of the supplied single-file portfolio. The original visual language is retained: same colors, typography, spacing, responsive breakpoints, animations, hover effects, portfolio filters, mobile menu, skill bars, and section layout.

## Quick start

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS/Linux/WSL
source .venv/bin/activate

pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`.

For production locally:

```bash
gunicorn app:app
```

## Where to edit things

- `content.py` — your text, portfolio items, skill percentages, services, contact details and social links.
- `templates/index.html` — page structure/HTML.
- `templates/partials/header.html` — navigation.
- `templates/partials/footer.html` — footer.
- `static/css/style.css` — styling.
- `static/js/main.js` — interactions and animations.
- `static/images/` — put your portfolio images here.
- `app.py` — Flask routes/backend.
- `render.yaml` — Render Blueprint.

## Adding an image

Put the image in `static/images/`, then change a portfolio item in `content.py`:

```python
{"t": "My Creature", "c": "sculpt", "g": ["#ff5c38", "#a56bff"], "image": "/static/images/my-creature.jpg"}
```

If `image` is empty, the original gradient placeholder is used.

## Render

Commit the project to GitHub, then in Render choose **New > Blueprint** and select the repository containing `render.yaml`. Render will create the web service from the YAML.

The Blueprint uses:

- Python runtime
- `pip install -r requirements.txt` build command
- Gunicorn with `app:app`
- `/health` health check
- generated `SECRET_KEY`

## Contact form

The Flask route receives the form, but this starter does not send email or save submissions to a database. Implement that in `app.py` when you choose an email provider or database.

## Architecture

```text
portfolio-flask/
├── app.py
├── content.py
├── requirements.txt
├── render.yaml
├── README.md
├── .gitignore
├── templates/
│   ├── base.html
│   ├── index.html
│   └── partials/
│       ├── header.html
│       └── footer.html
└── static/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── main.js
    ├── images/
    └── fonts/
```
