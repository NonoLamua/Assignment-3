from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to our Dockerized Web Application!"

@app.route('/about')
def about():
    return "This is a simple Flask app for Assignment 3."

if __name__ == '__main__':
    # Explicitly bind to port 8000 and listen on all interfaces (0.0.0.0)
    app.run(host='0.0.0.0', port=8000)

