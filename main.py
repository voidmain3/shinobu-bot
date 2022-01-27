import telebot
import requests

import os
my_secret = os.environ['key']
bot = telebot.TeleBot(my_secret)

url = "https://api.coindcx.com/exchange/ticker"

response = requests.get(url)
data = response.json()
print(data[0]['last_price'])

@bot.message_handler(commands=['list'])
def list(message):
  response = requests.get(url)
  data = response.json()
  inr_list = ''
  for target in data:
    if(target['market'].find('INR') > 0):
      inr_list += ' \n' + target['market']
  bot.reply_to(message, inr_list)
  print(inr_list)  

@bot.message_handler(commands=['get'])
def get(message):
  response = requests.get(url)
  data = response.json()
  re = message.text.split(' ')[1]
  print(re)
  send = '100'
  for target in data:
    if(target['market'] == re):
      send = target['last_price']
  bot.reply_to(message, send)
    



@bot.message_handler(commands=["greet"])
def greet(message):
  bot.reply_to(message, "hey how are you , this is a greet from the bot")

@bot.message_handler(commands=["hello"])
def hello(message):
  bot.send_message(message.chat.id, "this is a hello from bot")

def val(message):
  if len(message.text.split()) > 2:
    return True

@bot.message_handler(commands=["eval"])
def calc(message):  
  re = message.text.strip("/eval")
  bot.reply_to(message, eval(re))


bot.polling()