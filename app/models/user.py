from .base import BaseModel
from app import db


class User(BaseModel):
    __tablename__ = 'users'

    id = db.Column(db.String(100), unique=True, primary_key=True)
    email = db.Column(db.String(120))
    phone = db.Column(db.String(11), unique=True)
    password: db.Column(db.String(100))
    token: db.Column(db.String(100))
    avatar: db.Column(db.String(100))
    signature: db.Column(db.String(100))
    nick: db.Column(db.String(100))

    def __init__(self, username, email):
        self.username = username
        self.email = email
