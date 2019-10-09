import apiai
import json

def send_message(message):
    request = apiai.ApiAI("c5171fa796684170843bb6e598d8e380").text_request()
    request.lang = "ru"
    request.session_id = "session_id"
    request.query = message
    response = json.loads(request.getresponse().read().decode('utf-8'))
    print(response['result']['fulfillment']['speech'])
    return response ['result']['action']

print("Введите свое сообщение: ")
message = input()
actions = None
while True:
    actions = send_message(message)
    if actions == 'smalltalk.greetings.bye':
        break
    message = input()
