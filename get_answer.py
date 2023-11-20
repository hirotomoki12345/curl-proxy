from bardapi import Bard

def get_bard_answer(question):
    token = 'xxxxxxx'  # あなたのBard APIトークン
    bard = Bard(token=token)
    answer = bard.get_answer(question)['content']
    return answer
