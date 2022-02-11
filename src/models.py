from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)

    @classmethod
    def register(cls, new_user):
        new_user = cls(**new_user)
        db.session.add(new_user)
        
        try:
            db.session.commit()
            return new_user
        except Exception as error:
            db.session.rollback()
            return None

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username
            # do not serialize the password, its a security breach
        }