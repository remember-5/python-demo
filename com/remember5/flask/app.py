from flask import Flask, jsonify, request, redirect
app = Flask(__name__)
import sqlite3



@app.route('/')
def hello_world():
   return 'Hello World'


@app.route('/test')
def hello_test():
   return 'Hello Test'


@app.route('/upload', methods=['GET', 'POST'])
def upload():
   if request.method == 'POST':
      fs = request.files.getlist('files')  # 一次性多个文件
      print(fs)
   return "asd"

@app.route('/name/<name>')
def hello(name):
   # 保存数据库
   # age = 11
   # db.save(f"insert user(name,age) values(${name},${age}) ")

   return 'Hello' + name

if __name__ == '__main__':
   app.run()
   conn = sqlite3.connect('test.db')
   print("Opened database successfully")