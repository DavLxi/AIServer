from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许所有域名的跨域请求

source_server = 'http://152.136.37.136:3000'  # 目标服务器的 URL

# 接收请求并转发到其他服务器

# 本地的其他端点(test  测试接口)
@app.route('/local', methods=['GET'])
def local():
    return jsonify(message="This is a local response.")

# 登录接口
@app.route('/v1/api/user/auth/login', methods=['GET', 'POST', 'OPTIONS'])
def login():
    if request.method == 'OPTIONS':
        # 处理预检请求
        return jsonify(success=True)
    
    # 获取客户端发送的 JSON 数据
    data = request.get_json()

    url = source_server + data.get('interface')  # 目标服务器的 URL
    headers = {
        'Content-Type': 'application/json',
    }
    print(data)

    # 转发请求到目标服务器
    response = requests.post(url, json=data, headers=headers)

    # 返回目标服务器的响应
    return jsonify(response.json())


# 注册接口
@app.route('/v1/api/user/new', methods=['GET', 'POST', 'OPTIONS'])
def register():
    if request.method == 'OPTIONS':
        # 处理预检请求
        return jsonify(success=True)
    
    # 获取客户端发送的 JSON 数据
    data = request.get_json()

    url = source_server + data.get('interface')  # 目标服务器的 URL
    headers = {
        'Content-Type': 'application/json',
    }
    print(url)

    # 转发请求到目标服务器
    response = requests.post(url, json=data, headers=headers)

    # 返回目标服务器的响应
    return jsonify(response.json())

# 获取知识库列表
@app.route('/v1/api/knowledge_base/list', methods=['GET', 'POST', 'OPTIONS'])
def getKonwledgeList():
    if request.method == 'OPTIONS':
        # 处理预检请求
        return jsonify(success=True)

    # print(request)
    # 获取Authorization头部信息
    api_key = request.headers.get('Authorization')

    if not api_key:
        return jsonify({"error": "Authorization header is missing"}), 400

    url = source_server + '/v1/api/knowledge_base/list'  # 目标服务器的 URL
    headers = {
        'Content-Type': 'application/json',
        'Authorization': api_key  # 传递Authorization头部
    }
    
    response = requests.get(url, headers=headers)

    # 返回目标服务器的响应
    return jsonify(response.json())

# 新建知识库列表
@app.route('/v1/api/knowledge_base/new', methods=['GET', 'POST', 'OPTIONS'])
def createKonwledge():
    if request.method == 'OPTIONS':
        # 处理预检请求
        return jsonify(success=True)

    # 获取客户端发送的 JSON 数据
    data = request.get_json()

    # 获取Authorization头部信息
    api_key = data.get('Authorization')
    print(api_key)
    if not api_key:
        return jsonify({"error": "Authorization header is missing"}), 400

    url = source_server + data.get('interface')  # 目标服务器的 URL
    headers = {
        'Content-Type': 'application/json',
        'Authorization': api_key  # 传递Authorization头部
    }
    print(url)

    # 转发请求到目标服务器
    response = requests.post(url, json=data, headers=headers)

    # 返回目标服务器的响应
    return jsonify(response.json())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # 在本地 5000 端口运行
