# -*- coding: utf-8 -*-
# @Time    : 2019/1/11 22:45
# @Author  : Ming

from .. import app
from flask_sqlalchemy import SQLAlchemy
import pymssql


db = SQLAlchemy(app, use_native_unicode='utf8')
