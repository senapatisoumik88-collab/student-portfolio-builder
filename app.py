from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template(
        'index.html',
        name='Soumik Senapati',
        skill='Python, HTML, CSS, Flask',
        title='Personal Portfolio Website',
        github='https://github.com/yourgithubusername',
        linkedin='https://linkedin.com/in/yourlinkedinusername',
        photo='https://i.imgur.com/6VBx3io.png'
    )

if __name__ == '__main__':
    app.run(debug=True)
