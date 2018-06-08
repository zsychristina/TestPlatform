#coding=utf-8

from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template

from mongo import Mongo
from function import Function

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/coverage")
def coverage():
    return render_template("coverage.html")


@app.route("/function")
def function():
    return render_template("function.html")


@app.route("/function/api", methods=['POST'])
def function_handler():
    data = request.get_json()
    commands = data.pop('commands', None)
    if commands is None:
        return jsonify({
            'status': 1,
            'message': "错误的指令序列！",
            'data': data
        })

    func = Function(commands)
    func.run()

    return jsonify({
        'status': 1,
        'message': "success",
        'data': data
    })


@app.route("/interface")
def interface():
    return render_template("interface.html")


@app.route("/interface/handler", methods=['POST'])
def interface_handler():
    data = request.get_json()
    print data

    url = data.pop('url')
    method = data.pop('method')
    payload = data.pop('param')
    headers = data.pop('header')
    code = data.pop('code')

    if url is None or len(url) == 0:
        return jsonify({
            'status': 1,
            'message': "url format error!",
            'data': data
        })

    # 利用反射机制实例化请求
    module = __import__("requests")
    http = getattr(module, method)
    response = http(url, params=payload, headers=headers)

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

    exec(code, context)

    result = {
        'status': context['result']['status'],
        'message': context['result']['message'],
        'data': data
    }

    return jsonify(result)


"""
由此以下是数据增删改查接口
"""
@app.route('/api/v1/insert', methods=['POST'])
def insert():
    data = request.get_json()
    client = Mongo()
    collection = data.pop("collection", "user")
    result = client.insert("testfan", collection, data)
    if result is None:
        return jsonify({
            'status': 400,
            'message': '插入失败',
            'data': data
        })
    else:
        return jsonify({
            'status': 200,
            'message': '插入成功',
            'data': str(result)
        })


@app.route('/api/v1/delete', methods=['DELETE'])
def delete():
    data = request.get_json()
    client = Mongo()
    result = client.delete("testfan", "user", data)
    return jsonify({
        'status': 200,
        'message': '删除成功',
        'data': result
    })


@app.route('/api/v1/update', methods=['PUT'])
def update():
    data = request.get_json()
    client = Mongo()
    print data
    result = client.update("testfan", "user", data)
    print result
    return jsonify({
        'status': 200,
        'message': '更新成功',
        'data': result
    })


@app.route('/api/v1/search', methods=['GET'])
def search():
    data = request.values.to_dict()
    collection = data.pop('collection', 'user')
    client = Mongo()
    result = client.search("testfan", collection, data)
    # print result
    return jsonify({
        'status': 200,
        'message': '查询成功',
        'data': result
    })


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=9999,
        debug=True
    )