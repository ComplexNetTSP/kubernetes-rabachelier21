from flask import Flask
app = Flask(__name__)

@app.route("/")
def chall1():
    return ("<p>Raphaël Bachelier</p> <p>chall 1</p> <p>V1 du site</p> <p>PC de Raph</p> <p>14/01/2025</p>")
