import json


def text_message_by_language(language: str, message: str):
    with open('mics/messages.json') as file:
        data = json.load(file)
    return data[language][message]


def number_is_message(message: str):
    for i in message:
        if i not in '0123456789.,':
            return False
    try:
        message = float(message.replace(',', '.'))
        return True
    except ValueError:
        return False
