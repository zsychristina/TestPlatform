#coding=utf-8
import flask
from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
from pymongo import MongoClient
from mongo import Mongo
import inspect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/coverage')
def coverage():
    return render_template("coverage.html")


@app.route('/interface')
def interface():
    return render_template("interface.html")


@app.route('/interface/handler', methods=['POST'])
def interface_handler():
    data = request.get_json()
    print (data)
    url = data.pop('url')
    method = data.pop('method')
    payload = data.pop('param')
    headers = data.pop('header')
    code = data.pop('code')

    #利用发射实例化请求
    module = __import__("requests")
    http = getattr(module, method)
    response = http(url,params=payload,headers=headers)
    print (response)
    status = response.status_code
    data = response.json()

    context = {
        'response': {
            'status': status,
            'data': data,
        },
        'result': {
            'status': 0,
            'message': "success",
        }
    }

    exec (code, context)

    result = {
        'status': context['result']['status'],
        'message': context['result']['message'],
        'data': data
    }

    return jsonify(result)


@app.route('/function')
def function():
    return render_template("function.html")


@app.route('/performance',methods=['GET'])
def performance():
    return render_template("performance.html")


@app.route('/performance/handler', methods=['POST'])
def performance_handler():
    data = request.get_json()
    print (data)
    host = data.pop('host')
    user = data.pop('user')
    qps = data.pop('qps')
    count = data.pop('count')
    code = data.pop('code')

    # 进行压测
    with open ("locustfile.py",'w') as file:
        file.write(code)

    import subprocess
    cmd = 'locust -f locustfile.py --host='+host+' --csv=testfan --no-web -c'+user+' -r'+qps+' -n'+count
    process = subprocess.Popen(cmd)
    process.wait()

    import csv
    reader = csv.reader(open('C:/Users/chris/PycharmProjects/pandora/testfan_requests.csv', 'r'))
    result = list(reader)
    data.setdefalt('result',result)

    mongo = Mongo()
    mongo.insert('testfan','performance',data)

    return jsonify()



"""
由此一下为数据增删改查接口
"""

@app.route('/api/v1/insert', methods=['POST'])
def insert():
    data = request.get_json()       #接收mongo.js发送的请求数据
    client = Mongo()
    collection = data.pop("collection","user")
    result = client.insert("testfan", collection, data)
    if result is None:
        return jsonify({      #通过jsonify方法直接将dict类型转换为json串，jsonify是flask自带的json处理类，返回的为flask结果
            'status': 400,
            'message': "插入失败",
            'data': data
        })
    else:
        return jsonify({
            'status': 200,
            'message': "插入成功",
            'data': str(result)
        })


@app.route('/api/v1/delete', methods=['DELETE'])
def delete():
    data = request.get_json()
    client = Mongo()
    result = client.delete("testfan", "user", data)
    if result is None:
        return jsonify({
            'status': 400,
            'message': "删除失败",
            'data': data
        })
    else:
        return jsonify({
            'status': 200,
            'message': "删除成功",
            'data': str(result)
        })


@app.route('/api/v1/search',methods=['GET'])
def search():
    data = request.values.to_dict()
    collection = data.pop('collection','user')
    client = Mongo()
    result = client.search("testfan", collection, data)
    if result is None:
        return jsonify({
            'status': 400,
            'message': "查询失败",
            'data': data
        })
    else:
        return jsonify({
            'status': 200,
            'message': "查询成功",
            'data': result
        })


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=9999,
        debug=True,
    )

