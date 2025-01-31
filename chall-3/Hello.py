from flask import Flask, request
from pymongo import MongoClient
from datetime import datetime


app = Flask(__name__)

MONGO_HOST = 'mongodb'
MONGO_PORT = 27017

client = MongoClient(MONGO_HOST, MONGO_PORT)
db = client['MyMongoDB']
visit_logs_collection = db['visit_logs']
 

@app.route("/")
def hello_world():
    
    client_ip = request.remote_addr
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    visit_logs_collection.insert_one({'ip_address': client_ip, 'visit_date': current_date})
    last_records = list(visit_logs_collection.find().sort([("_id", -1)]).limit(10))
    
    html = """
    <h1>BACHELIER Raphaël</h1>
    <h1> Projet : Applidocker</h1>
    <h1> Version : V2</h1>
    <h1> Server hostname : monordi</h1>
    <h1> Date : 28/01/2025 </h1>
    <h1>Last 10 Visitor Logs:</h1>
    """
    for record in last_records:
        html += f"<p>IP Address: {record['ip_address']} - Visit Date: {record['visit_date']}</p>"

    return html