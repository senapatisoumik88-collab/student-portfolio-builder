rom flask import Flask, render_template, request
import os

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Create portfolio page
@app.route("/create")
def create():
    return render_template("create.html")


# Generate AI portfolio
@app.route("/generate-ai", methods=["POST"])
def generate_ai():

    name = request.form.get("name")
    skills = request.form.get("skills")
    projects = request.form.get("projects")

    result = f"""
    <html>
    <head>
        <title>{name}'s Portfolio</title>
    </head>

    <body style="font-family:Arial; padding:40px;">

    <h1>{name}'s AI Generated Portfolio</h1>

    <p><b>Bio:</b> Passionate developer skilled in {skills}.</p>

    <p><b>Skills:</b> {skills}</p>

    <p><b>Projects:</b> {projects}</p>

    <h3>Example Projects</h3>

    <ul>
        <li>Portfolio Builder Website</li>
        <li>Flask Web Application</li>
        <li>AI Student Tool</li>
    </ul>

    <br>

    <button onclick="window.print()">Download Portfolio</button>

    </body>
    </html>
    """

    return result


if _name_ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
