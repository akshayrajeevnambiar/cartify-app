from src import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), default='user')

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.name,
            "password": self.password
        }
