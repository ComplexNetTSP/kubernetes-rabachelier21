from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
    <h1>BACHELIER Raphaël</h1>
    <h1> Projet : App</h1>
    <h1> Version : V2</h1>
    <h1> Server hostname : monordi</h1>
    <h1> Date : 29/01/2025 </h1>
    <h1>Last 10 Visitor Logs:</h1>
    """