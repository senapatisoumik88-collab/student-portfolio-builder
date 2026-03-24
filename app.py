from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('create.html')

@app.route('/generate', methods=['POST'])
def generate():
    name = request.form.get('name')
    skill = request.form.get('skill')
    title = request.form.get('title')
    photo = request.form.get('photo')
    github = request.form.get('github')
    linkedin = request.form.get('linkedin')

    # ✅ JPG/JPEG validation
    if not re.search(r"\.(jpg|jpeg)$", photo, re.IGNORECASE):
        return "❌ Error: Only JPG/JPEG image URL allowed!"

    return render_template(
        'portfolio.html',
        name=name,
        skill=skill,
        title=title,
        photo=photo,
        github=github,
        linkedin=linkedin
    )

if __name__ == '__main__':
    app.run(debug=True)
