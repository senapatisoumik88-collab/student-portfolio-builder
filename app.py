from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('create.html')


# Generate Portfolio Page
@app.route('/generate', methods=['POST'])
def generate():

    # Get Form Data
    name = request.form.get('name')
    skill = request.form.get('skill')
    title = request.form.get('title')
    photo = request.form.get('photo')
    github = request.form.get('github')
    linkedin = request.form.get('linkedin')

    # Validation
    if not name or not skill or not title:
        return "❌ Please fill all required fields."

    # Image validation
    if not re.search(r'\.(jpg|jpeg|png)$', photo, re.IGNORECASE):
        return "❌ Only JPG, JPEG or PNG image links are allowed."

    # GitHub validation
    if "github.com" not in github:
        return "❌ Please enter a valid GitHub link."

    # LinkedIn validation
    if "linkedin.com" not in linkedin:
        return "❌ Please enter a valid LinkedIn link."

    # Render Portfolio
    return render_template(
        'portfolio.html',
        name=name,
        skill=skill,
        title=title,
        photo=photo,
        github=github,
        linkedin=linkedin
    )


# Error Handling
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


# Run App
if __name__ == '__main__':
    app.run(debug=True)
