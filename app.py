from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "¡Hola desde GitHub Codespaces!!!!"


@app.route('/adios')
def goodbye():
    return '¡Adiós desde GitHub Codespaces!'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
