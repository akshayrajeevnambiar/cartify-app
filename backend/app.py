# This folder would be the main entry point of the application
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home() :
    return "Welcome to Cartify"

if __name__ == '__main__':
    app.run(debug=True)