from flask import Flask, request, jsonify
import subprocess

app = Flask(__name)

@app.route('/')
def index():
    return open("index.html").read()

@app.route('/get_data', methods=['POST'])
def get_data():
    try:
        data = request.get_json()
        url = data['url']

        # Curlを使用して指定したURLからデータを取得
        result = subprocess.check_output(['curl', url], text=True)

        return result
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run()
