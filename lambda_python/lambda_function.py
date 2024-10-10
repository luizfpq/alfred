
from httplib2 import Http
from json import dumps

def lambda_handler(event, context):
    url = "https://chat.googleapis.com/v1/spaces/AAAAbNNAFoo/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=9EIciAPnLM-ACoHncaI2RGF-NETCpsJSZ4xSoo6WDBQ"
    bot_message = {'text' : event['Records'][0]['Sns']['Message']}
    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    http_obj = Http()
    response = http_obj.request(
            uri=url,
            method='POST',
            headers=message_headers,
            body=dumps(bot_message),
        )
    return response
