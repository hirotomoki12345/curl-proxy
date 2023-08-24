from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetchData', methods=['POST'])
def fetch_data():
    try:
        url = request.json['url']
        # Use curl to fetch website data
        curl_command = f'curl {url}'
        result = subprocess.run(curl_command.split(), stdout=subprocess.PIPE)
        fetched_data = result.stdout.decode('utf-8')
        return fetched_data
    except Exception as e:
        return f'Error fetching data: {e}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
