from app.main import app

if name == 'main':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)