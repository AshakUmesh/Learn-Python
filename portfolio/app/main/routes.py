from flask import Blueprint, render_template

main = Blueprint("main", __name__)


@main.route("/")
def index():
    """Home page showing hero section and about info."""
    return render_template("index.html")


@main.route("/projects")
def projects():
    """Projects page listing portfolio projects."""
    return render_template("projects.html")



@main.route("/contact")
def contact():
    """Contact page with simple contact information/CTA."""
    return render_template("contact.html")

@main.route("/resume")
def resume():
    """Resume / CV page."""
    return render_template("resume.html")

@main.route("/skills")
def skills():
    """Technical skills page."""
    return render_template("skills.html")

@main.route("/about")
def about():
    """About / bio page."""
    return render_template("about.html")