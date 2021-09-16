from flask import Flask,jsonify,request

app = Flask(name)
CORS(app)
@app.route('/')

def index():
    return "<h1>Skripsi-XGBoost-app !!</h1>"