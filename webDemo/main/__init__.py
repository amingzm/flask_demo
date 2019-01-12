# -*- coding: utf-8 -*-
# @Time    : 2019/1/12 18:20
# @Author  : Ming
from flask import Flask

app = Flask(__name__)
app.config.from_object('main.config')

from .routes import *
