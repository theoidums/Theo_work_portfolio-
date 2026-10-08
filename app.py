from flask import Flask, render_template, request
from content import (
    SITE, HERO, DISCIPLINES, WORKS, PORTFOLIO_CATEGORIES, ABOUT, SKILLS,
    SERVICES, EXPERIENCE, EDUCATION, SOCIALS, CONTACT,
)

app = Flask(__name__)
app.config["SECRET_KEY"] = __import__("os").environ.get("SECRET_KEY", "dev-only-change-me")


def page_context(**extra):
    context = {
        "site": SITE,
        "hero": HERO,
        "disciplines": DISCIPLINES,
        "works": WORKS,
        "portfolio_categories": PORTFOLIO_CATEGORIES,
        "about": ABOUT,
        "skills": SKILLS,
        "services": SERVICES,
        "experience": EXPERIENCE,
        "education": EDUCATION,
        "socials": SOCIALS,
        "contact": CONTACT,
        "form_message": "",
    }
    context.update(extra)
    return context


@app.get("/")
def home():
    return render_template("index.html", **page_context())


@app.post("/contact")
def contact():
    # This is intentionally kept simple. Add email/DB handling here later.
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        return render_template(
            "index.html",
            **page_context(form_message="Please complete the required fields."),
        ), 400

    # TODO: send/store the message. Do not pretend it was emailed yet.
    return render_template(
        "index.html",
        **page_context(form_message="Thanks! Your message was received by the site."),
    )


@app.get("/health")
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    app.run(debug=True)
