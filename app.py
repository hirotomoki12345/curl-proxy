from flask import Flask, request

app = Flask(__name)

@app.route('/')
def index():
    return open("index.html").read()

@app.route('/get_data', methods=['GET'])
def get_data():
    return "This is a response from the server."

if __name__ == '__main__':
    app.run()
