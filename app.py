from flask import Flask,jsonify,request

app = Flask(__name__)
#CORS(app)
@app.route('/')

def index():
    return "<h1>Skripsi-XGBoost-app !!</h1>"