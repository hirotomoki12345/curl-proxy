from flask import Flask, request, Response
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import base64
import socks
import socket

app = Flask(__name__)

socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
socket.socket = socks.socksocket

@app.route('/')
def home():
    return """
    <html>
    <head>
    <title>Proxyサイト</title>
    <style>
    body {
        font-family: Arial, sans-serif;
        margin: 20px;
    }
    form {
        margin-bottom: 20px;
    }
    input[type="text"] {
        width: 400px;
        padding: 5px;
        font-size: 16px;
    }
    button {
        padding: 5px 10px;
        font-size: 16px;
        cursor: pointer;
    }
    </style>
    </head>
    <body>
    <h1>Proxyサイトへようこそ</h1>
    <form action="/proxy" method="get">
        <input type="text" name="url" placeholder="URLを入力してください">
        <button type="submit">取得</button>
    </form>
    </body>
    </html>
    """

@app.route('/proxy', methods=['GET'])
def proxy():
    url = request.args.get('url', '')
    if not url:
        return "URLが指定されていません", 400

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for tag in soup.find_all('a', href=True):
        tag['href'] = '/proxy?url=' + urljoin(url, tag['href'])
    for tag in soup.find_all(['link', 'img'], src=True):
        if not tag['src'].startswith(('http://', 'https://')):
            resource_url = urljoin(url, tag['src'])
            resource_response = requests.get(resource_url)
            content_type = resource_response.headers.get('content-type', 'application/octet-stream')
            if 'text' in content_type or 'html' in content_type:
                tag['src'] = f'data:{content_type};base64,{base64.b64encode(resource_response.content).decode()}'
            else:
                tag['src'] = resource_url
    for tag in soup.find_all('link', rel='stylesheet', href=True):
        if not tag['href'].startswith(('http://', 'https://')):
            resource_url = urljoin(url, tag['href'])
            resource_response = requests.get(resource_url)
            content_type = resource_response.headers.get('content-type', 'text/css')
            tag['href'] = f'data:{content_type};base64,{base64.b64encode(resource_response.content).decode()}'

    for script_tag in soup.find_all('script', src=True):
        if not script_tag['src'].startswith(('http://', 'https://')):
            script_url = urljoin(url, script_tag['src'])
            script_response = requests.get(script_url)
            script_content_type = script_response.headers.get('content-type', 'application/javascript')
            script_tag['src'] = f'data:{script_content_type};base64,{base64.b64encode(script_response.content).decode()}'

    response = Response(str(soup))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
    app.run(debug=True)
