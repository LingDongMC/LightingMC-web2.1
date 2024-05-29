from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
import sqlite3

app = Flask(__name__, static_url_path='/static')
CORS().init_app(app)
# 假设这是一个简单的用户数据库
users = {
    "user1": {"username": "user1", "password": "password1"},
    "user2": {"username": "user2", "password": "password2"}
}


def get_data_from_database(table_name):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM {}".format(table_name))
    data = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    result = []
    for row in data:
        result.append(dict(zip(columns, row)))
    conn.close()
    return result


@app.route('/data/<table_name>')
def get_data(table_name):
    data = get_data_from_database(table_name)
    # 将数据转换为 JSON 格式并返回
    return jsonify(data)


# 路由来处理登录请求
@app.route('/login', methods=['POST', 'GET'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username]['password'] == password:
        # 认证成功，生成并返回访问令牌（JWT）
        return jsonify({"access_token": "your_generated_jwt_token"})
    else:
        return jsonify({"error": "Invalid username or password"}), 401


@app.route('/get_image_url/<filename>')
def get_image_url(filename):
    image_url = f'/images/{filename}'
    return jsonify({'image_url': image_url})


# 假设图片存储在 'uploads' 目录中
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/image/<filename>')
def get_image(filename):
    return send_from_directory('static/images', filename)


if __name__ == '__main__':
    app.run(debug=True)
