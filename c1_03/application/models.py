# -*- encoding=UTF-8 -*-

from application import db
import random
class User(db.Model):
    id = db.Colum(db.Integer, primary_key=True, autoincrement=True)
    username = db.Colum(db.String(80), unique = True)
    password = db.Colum(db.String(32))
    head_url = db.Colum(db.String(256))


    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.head_url = 'http://images.nowcoder.com/head/'+ str(random.randint)

    def __repr__(self):
        return '<User %d &s>'%(self.id, self.username)