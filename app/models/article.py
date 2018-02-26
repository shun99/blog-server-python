from .base import BaseModel
from app import db


class Article(BaseModel):
    __tablename__ = 'articles'

    id = db.Column(db.String(100), unique=True, primary_key=True)
    title = db.Column(db.TEXT)
    des = db.Column(db.TEXT)
    content = db.Column(db.TEXT)
