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

    # VULNERABILITE VOLONTAIRE POUR LE TP
    # Une entrée utilisateur est transmise directement au shell.
   result = subprocess.run(
     "ping -n 1 " + host,
     shell=True,
     capture_output=True,
     text=True
)
    )

    return f"<pre>{result.stdout}</pre>"


if __name__ == "__main__":
    app.run(debug=False)