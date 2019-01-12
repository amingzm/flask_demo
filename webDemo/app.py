from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import pymssql
app = Flask(__name__)
app.config.from_object('main.config.config')

'''
class Task1(db.Model):
    Task = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)

    def __init__(self, age):
        self.age = age

    def __repr__(self):
        return '<age %d>' % self.age
'''

@app.route('/')
def hello_world():
    taskA = Task1(20)
    db.session.add(taskA)
    db.session.commit()
    # 查询
    myData = Task1.query.all();
    output = []
    for data in myData:
        r_data = {}
        r_data['id'] = data.Task
        r_data['age'] = data.age
        output.append(r_data)
    return jsonify({'message': output})
    # return "hello world"


if __name__ == '__main__':
    app.run(debug=True, port=5000)


