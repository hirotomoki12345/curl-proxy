from flask import Flask, request, jsonify
from bardapi import Bard

app = Flask(__name__)

token = 'cQi2uJoenm91t7F3tZO7qet54AK-zydIxB6FufuGH3UDZbwSPdf3n5ZTvMcUC65zHZZrRA.'
bard = Bard(token=token)

@app.route('/get_answer', methods=['POST'])
def get_answer():
    data = request.get_json()
    question = data['question']
    answer = bard.get_answer(question)['content']
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
