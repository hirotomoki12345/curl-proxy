from flask import Flask, request, jsonify
import requests

app = Flask(__name)

@app.route('/')
def index():
    return open("index.html").read()

@app.route('/fetch_data', methods=['POST'])
def fetch_data():
    try:
        url = request.json['url']
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return "Failed to fetch data from the URL."
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run()
