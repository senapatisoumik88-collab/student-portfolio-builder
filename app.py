from flask import Flask, render_template, request

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('create.html')


# Generate Portfolio
@app.route('/generate', methods=['POST'])
def generate():

    # Get form data
    name = request.form.get('name')
    skill = request.form.get('skill')
    title = request.form.get('title')
    photo = request.form.get('photo')
    github = request.form.get('github')
    linkedin = request.form.get('linkedin')

    # Render portfolio page
    return render_template(
        'portfolio.html',
        name=name,
        skill=skill,
        title=title,
        photo=photo,
        github=github,
        linkedin=linkedin
    )


# Custom 404 Page
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


# Run Flask App
if __name__ == '__main__':
    app.run(debug=True)
