from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/portfolio", methods=["POST"])
def portfolio():
    name = request.form["name"]
    skills = request.form["skills"]
    project = request.form["project"]
    github = request.form["github"]
    linkedin = request.form["linkedin"]
    photo = request.form["photo"]

    return render_template(
        "portfolio.html",
        name=name,
        skills=skills,
        project=project,
        github=github,
        linkedin=linkedin,
        photo=photo
    )

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
