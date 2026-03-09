from flask import Flask, render_template, request
import os

app = Flask(_name_)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/create")
def create():
    return render_template("create.html")


@app.route("/generate-ai", methods=["POST"])
def generate_ai():

    name = request.form.get("name")
    skills = request.form.get("skills")
    projects = request.form.get("projects")

    return f"""
    <html>
    <head>
        <title>{name}'s Portfolio</title>
    </head>

    <body style="font-family:Arial; padding:40px;">

    <h1>{name}'s AI Generated Portfolio</h1>

    <p><b>Bio:</b> Passionate developer skilled in {skills}.</p>

    <p><b>Skills:</b> {skills}</p>

    <p><b>Projects:</b> {projects}</p>

    <ul>
        <li>Portfolio Builder Website</li>
        <li>Flask Web App</li>
        <li>AI Student Tool</li>
    </ul>

    <br>

    <button onclick="window.print()">Download Portfolio</button>

    </body>
    </html>
    """


if _name_ == "_main_":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
