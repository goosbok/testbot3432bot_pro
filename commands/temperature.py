import requests

def temper(bot, update, city):
    try:
        url = 'http://api.openweathermap.org/data/2.5/find'
        API_ID = '7802b89f71644561ca3d6b42087ebaea'
        data = {
            'q':city,
            'appid':API_ID
        }
        r = requests.get(url, params = data)
        json = r.json()
        return str((int(json['list'][0]['main']['temp']) - 273)) + ' C'
    except:
        bot.send_message(chat_id=update.message.chat_id, text='Что-то пошло не так')