from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

# 后端接收到的请求方式：POST
@app.route('/login', methods=['POST'])
def login():
    # 获取前端传来的数据
    data = request.get_json()

    # 获取账号、密码、请求方式和接口地址
    username = data.get('name')
    password = data.get('password')
    request_url = data.get('url')
    request_endpoint = data.get('endpoint')

    # 构建远程服务器请求的完整 URL
    url = f'{request_url}{request_endpoint}'

    # 请求体数据
    payload = {
        "name": username,
        "password": password
    }

    # 请求头部
    headers = {
        'Content-Type': 'application/json',
    }

    # 发送请求到远程服务器
    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        response.raise_for_status()  # 如果状态码不是 200 会抛出异常
        # 返回远程服务器的响应数据
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        # 错误处理：返回错误信息
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    # 运行服务器，监听端口 5000
    app.run(debug=True, host='0.0.0.0', port=5000)
