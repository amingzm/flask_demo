# -*- coding: utf-8 -*-
# @Time    : 2019/1/13 18:52
# @Author  : Ming
from . import db


class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_name = db.Column(db.String(64), index=True, unique=True)
    category_url = db.Column(db.String(64), unique=True)


class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    article_name = db.Column(db.String(64), index=True)
    article_url = db.Column(db.String(64), index=True)
    article_text = db.Column(db.Text)
    category_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    category = db.relationship('Item', backref=db.backref('articles'))
