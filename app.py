from flask import Flask,jsonify,request

app = Flask(name)
CORS(app)
@app.route('/')

def index():
    return "<h1>Skripsi-XGBoost-app !!</h1>"

if name == 'main':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)