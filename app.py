from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create uploads folder automatically
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/create')
def create():
    return render_template('create.html')


@app.route('/portfolio', methods=['POST'])
def portfolio():

    name = request.form['name']
    skills = request.form['skills']
    project = request.form['project']
    github = request.form['github']
    linkedin = request.form['linkedin']

    photo = request.files['photo']

    filename = secure_filename(photo.filename)

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    photo.save(filepath)

    return render_template(
        'portfolio.html',
        name=name,
        skills=skills,
        project=project,
        github=github,
        linkedin=linkedin,
        photo='uploads/' + filename
    )


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)