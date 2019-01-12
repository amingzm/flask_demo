# -*- coding: utf-8 -*-
# @Time    : 2019/1/11 22:45
# @Author  : Ming

from flask_sqlalchemy import SQLAlchemy
from ... import app


db = SQLAlchemy(app, use_native_unicode='utf8')
