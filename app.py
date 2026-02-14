from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate-ai", methods=["POST"])
def generate_ai():
    data = request.get_json()
    skills = data.get("input", "")

    result = f"""
    <h2>AI Generated Portfolio</h2>
    <p><b>Bio:</b> Passionate developer skilled in {skills}.</p>
    <p><b>Skills:</b> {skills}</p>
    <p><b>Projects:</b></p>
    <ul>
        <li>Portfolio Builder Website</li>
        <li>Flask Web App</li>
        <li>AI Student Tool</li>
    </ul>
    """

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True, port=5001)