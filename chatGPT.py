import requests
from credentials import chatGPTtoken


def talk_to_chatGPT(message):
    url = 'https://api.openai.com/v1/chat/completions'
    headers = {'Authorization': f'Bearer {chatGPTtoken}',
               'Content-Type': 'application/json'}
    body = {'model': 'gpt-3.5-turbo',
            'messages': [{'role': 'user', 'content': message}]}
    res = requests.post(url, headers=headers, json=body)
    return res.json()['choices'][0]['message']['content']