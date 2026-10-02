from flask import Flask, request
import subprocess

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>TP DevSecOps - Sécurité Web</h1>
    <p>Application Flask</p>
    <p><a href="/ping?host=127.0.0.1">Test réseau</a></p>
    """


@app.route("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")

    # Correction : aucun shell n'interprète l'entrée utilisateur.
    result = subprocess.run(
        ["ping", "-n", "1", host],
        shell=False,
        capture_output=True,
        text=True
    )

    return f"<pre>{result.stdout}</pre>"


if __name__ == "__main__":
    app.run(debug=False)