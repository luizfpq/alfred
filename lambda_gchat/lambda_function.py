import json
import os
import urllib.request

def lambda_handler(event, context):
    # Verificar se o evento é uma mensagem do Google Chat
    if event.get('httpMethod') == 'POST' and event.get('body'):
        body = json.loads(event['body'])

        # Verificar se é um evento de mensagem do Google Chat
        if body.get('type') == 'ADDED_TO_SPACE' or body.get('type') == 'MESSAGE':
            message = body.get('message', {}).get('text', '')
            sender = body.get('message', {}).get('sender', {}).get('displayName', '')

            if message:
                print(f"Mensagem recebida de {sender}: {message}")

                # Aqui você pode processar a mensagem e enviar uma resposta, se necessário
                response_message = f"Olá {sender}, obrigado pela sua mensagem!"
                send_message_to_chat(response_message, body.get('message', {}).get('thread', {}))

    return {
        'statusCode': 200,
        'body': 'OK'
    }

def send_message_to_chat(message, thread):
    webhook_url = "<url do webhook do gchat>"

    payload = {
        "text": message,
        "thread": thread
    }
    headers = {'Content-Type': 'application/json'}

    import requests
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)

    if response.status_code == 200:
        print("Mensagem enviada com sucesso para o Google Chat")
    else:
        print(f"Erro ao enviar mensagem para o Google Chat: {response.status_code} - {response.text}")