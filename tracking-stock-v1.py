import telebot
import time
import requests
import json

bot = telebot.TeleBot('1657483654:AAGypk9Nl115uMhUH6PoubUUVtx2QHw5BQs')
symbol = None
def find_symbol(msg):#cerca ! in testo
    for text in msg:
        if '!' in text:
            return text

@bot.message_handler(commands=['start'])#messaggio di benvenuto (/start)
def send_welcome(message):
    first_name = message.from_user.first_name
    welcome_message = "<b>Benvenuto {}!</b> \n\nSe vuoi cercare il prezzo di un'azione ti basterà fare <b>!nomeazione</b>.".format(first_name)
    bot.reply_to(message, welcome_message, parse_mode='HTML')

@bot.message_handler(func=lambda msg: msg.text is not None and '!' in msg.text)
def at_answer(message):
    texts = message.text.split()
    symbol = find_symbol(texts)[1:].upper()
    print(symbol)
    # bot.reply_to(message, 'Il prezzo che vuoi cercare è : <b>{}</b>' .format(symbol), parse_mode='HTML')

    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"

    querystring = {"region":"US","symbols":symbol}

    headers = {
        'x-rapidapi-key': "2c6c09100emsh27e1262ff540f02p1c0086jsn0a5ed3415ec2",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    
    full_response = response.text
    result = json.loads(full_response)
    market_price = result['quoteResponse']['result'][0]['regularMarketPrice']#printa prezzo
    bot.reply_to(message, '<b>{}</b> ha un prezzo di {}$ per azione.' .format(symbol, market_price), parse_mode='HTML')


    if(response.code == 200):
        return response.body
    else:
        return None


   
while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)

















