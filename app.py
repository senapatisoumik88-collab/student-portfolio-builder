from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate-ai", methods=["POST"])
def generate_ai():

    name = request.form.get("name")
    skills = request.form.get("skills")
    projects = request.form.get("projects")

    photo = request.files.get("photo")
    photo_filename = None

    if photo and photo.filename != "":
        photo_filename = photo.filename
        photo.save(os.path.join(app.config["UPLOAD_FOLDER"], photo_filename))

    return render_template(
        "portfolio.html",
        name=name,
        skills=skills,
        projects=projects,
        photo=photo_filename
    )

if __ == "__main__":
    app.run()
