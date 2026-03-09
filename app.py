from flask import Flask, render_template, request

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Create page
@app.route("/create")
def create():
    return render_template("create.html")

# AI generate route

@app.route("/generate-ai", methods=["POST"])
def generate_ai():
    name = request.form.get("name")
    skills = request.form.get("skills")
    projects = request.form.get("projects")

    result = f"""
<h2>{name}'s AI Generated Portfolio</h2>
<p><b>Bio:</b> Passionate developer skilled in {skills}.</p>
<p><b>Skills:</b> {skills}</p>
<p><b>Projects:</b> {projects}</p>

<ul>
<li>Portfolio Builder Website</li>
<li>Flask Web App</li>
<li>AI Student Tool</li>
</ul>
"""

    return result

import os

if __name__ =="__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
