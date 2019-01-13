# -*- coding: utf-8 -*-
# @Time    : 2019/1/12 16:52
# @Author  : Ming
from . import app
from flask import jsonify, request, render_template, session, abort, flash, redirect, url_for
from .model.post import Post
from .model.category import Category
from .model.entries import *
from .model import db


# http://docs.jinkan.org/docs/flask/index.html教程学习

@app.route('/')
def show_entries():
    entries = Entry.query.order_by(Entry.id.desc()).all()
    output = []
    for data in entries:
        r_data = {}
        r_data['titile'] = data.title
        r_data['text'] = data.text
        output.append(r_data)
    return render_template('show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)  # 放弃请求并返回错误代码
    entries_new = Entry(request.form['title'], request.form['text'])
    db.session.add(entries_new)
    db.session.commit()
    flash('New entry wa successfully posted!')
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True #键值对
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


# -------------------
# 入口测试
@app.route('/hello')
def hello_world():
    return 'hello_world'


# 建表
@app.route('/db/table/create')
def db_create():
    db.create_all()
    return '建表成功'


# -----------
# 数据库测试
@app.route('/dbtest', methods=['GET'])
def db_test():
    # 查询
    myData = Category.query.all()
    output = []
    print(len(myData))
    for data in myData:
        r_data = {}
        r_data['id'] = data.id
        r_data['name'] = data.name
        output.append(r_data)
    return jsonify({'message': output})
    # return "hello world"


@app.route('/db/category', methods=['POST', 'GET'])
def db_add():
    # 添加
    demo = Post("a", 'cc', Category('bb'), pub_date=None)
    db.session.add(demo)
    db.session.commit()

    # 修改
    myData = Category.query.all()
    print('修改前元素个数为：%d' % len(myData))
    demo.body = 'dd'
    db.session.commit()
    myData = Category.query.all()
    print('修改后元素个数：%d' % len(myData))

    # 删除
    db.session.delete

    if request.method == 'GET':
        return '请求成功'
    return 'POST请求'


# 定义404页面
@app.errorhandler(404)
def page_not_found(error):
    return '404'


@app.errorhandler(502)
def server_502_error(error):
    return '502'
