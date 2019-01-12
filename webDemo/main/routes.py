# -*- coding: utf-8 -*-
# @Time    : 2019/1/12 16:52
# @Author  : Ming
from . import app
from flask import jsonify
from .model.category import Category


@app.route('/a')
def hello_world():
    return 'hello_world'


@app.route('/dbtest', methods=['GET'])
def db_test():
    # 查询
    myData = Category.query.all()
    output = []
    for data in myData:
        r_data = {}
        r_data['id'] = data.id
        r_data['name'] = data.name
        output.append(r_data)
    return jsonify({'message': output})
    # return "hello world"


# 定义404页面
@app.errorhandler(404)
def page_not_found(error):
    return '404'


@app.errorhandler(502)
def server_502_error(error):
    return '502'
