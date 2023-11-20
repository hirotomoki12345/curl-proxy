from bardapi import Bard

def handler(event, context):
    token = 'cQi2uJoenm91t7F3tZO7qet54AK-zydIxB6FufuGH3UDZbwSPdf3n5ZTvMcUC65zHZZrRA.'
    bard = Bard(token=token)
    question = event['queryStringParameters']['question']
    answer = bard.get_answer(question)['content']

    return {
        'statusCode': 200,
        'body': answer
    }
