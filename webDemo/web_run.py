# -*- coding: utf-8 -*-
# @Time    : 2019/1/12 18:18
# @Author  : Ming

from main import app

if __name__ == "__main__":
    app.debug = app.config['DEBUG']
    app.run(debug=True, port=5000, host='127.0.0.1')