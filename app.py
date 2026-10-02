from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>TP DevSecOps - Sécurité Web</h1>
    <p>Application Flask</p>
    """


if __name__ == "__main__":
    app.run(debug=True)