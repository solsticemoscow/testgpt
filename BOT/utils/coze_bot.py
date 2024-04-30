import json, re


import requests

from BOT.config import COZE_BOT_ID, COZE


class Coze:


    def get_chat(self, QUERY: str):


        url = "https://api.coze.com/open_api/v2/chat"

        payload = json.dumps({
            "conversation_id": "123",
            "bot_id": f"{COZE_BOT_ID}",
            "user": "29032201862555",
            "query": QUERY,
            "stream": False
        })
        headers = {
            'Authorization': f'Bearer {COZE}',
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Host': 'api.coze.com',
            'Connection': 'keep-alive'
        }

        response = requests.post(url, headers=headers, data=payload)
        print(response.json())


        try:
            CONV_ID = response.json()['conversation_id']
            ANSWER = response.json()['messages'][0]['content']
            return ANSWER
        except Exception as e:
            return e








LLM = Coze()



