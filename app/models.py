from . import db

class User(db.Model):
    _tablename__ = 'users'
    phone_number = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))

    def __repr__(self):
        return f'User {self.username}'
