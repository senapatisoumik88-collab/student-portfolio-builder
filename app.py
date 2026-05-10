from flask import Flask, render_template, request

app = Flask(__name__)


# HOME PAGE
@app.route('/')
def home():
    return render_template('index.html')


# CREATE PORTFOLIO PAGE
@app.route('/create')
def create():
    return render_template('create.html')


# GENERATE PORTFOLIO
@app.route('/portfolio', methods=['POST'])
def portfolio():

    name = request.form['name']
    skills = request.form['skills']
    project = request.form['project']
    github = request.form['github']
    linkedin = request.form['linkedin']

    return render_template(
        'portfolio.html',
        name=name,
        skills=skills,
        project=project,
        github=github,
        linkedin=linkedin
    )


# CUSTOM 404 PAGE
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)