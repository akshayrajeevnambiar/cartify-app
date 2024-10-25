# This folder would be the main entry point of the application
from flask import Flask

#import os to get the enviroment variable
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__)

# Set up configuration using environment variables
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

@app.route("/")
def home() :
    return "Welcome to Cartify"

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)