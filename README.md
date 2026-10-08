# Portfolio Flask

A lightweight Flask conversion of the original one-page portfolio.

## Quick start

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`.

## Where to edit your portfolio

Start with:

```text
content.py
```

It contains structured sections for:

- site identity
- hero
- disciplines
- projects
- about
- skills
- services
- experience
- education
- social links
- contact

Put project images in:

```text
static/images/projects/
```

## Full guide

See **[PROJECT_GUIDE.md](PROJECT_GUIDE.md)** for the complete file structure, content model, project/image instructions, local setup, and Render deployment workflow.

## Render

The repository includes `render.yaml` for a Flask web service using Gunicorn.
