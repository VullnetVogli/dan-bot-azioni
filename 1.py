import requests
from bs4 import BeautifulSoup
import smtplib
from telepot.loop import MessageLoop
import telepot

API_KEY = '1657483654:AAGypk9Nl115uMhUH6PoubUUVtx2QHw5BQs'
bot = telepot.Bot(API_KEY)

URL = 'https://finance.yahoo.com/quote/ADA-USD?p=ADA-USD&.tsrc=fin-srch'

headers = {
    "User_Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81'
    }

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    price = float(soup.find(attrs = {'class': "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"}).get_text())

    if price < 1.18:
        bot.sendMessage(498686397, 'Prezzo sceso!')
        print('Prezzo sceso!')

print('Sto checkando.')

while True:
    check_price()





