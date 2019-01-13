# -*- coding: utf-8 -*-
# @Time    : 2019/1/12 22:12
# @Author  : Ming
from . import db


class Entry(db.Model):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80))
    text = db.Column(db.Text)

    def __init__(self, title, text):
        self.title = title
        self.text = text

    def __repr__(self):
        return '<User %r>' % self.title
