from flask_sqlalchemy import SQLAlchemy
# 创建对象
db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(20),unique=True)
    password = db.Column(db.String(100))