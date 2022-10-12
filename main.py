import telebot
import requests

import os
my_secret = os.environ.get('API_KEY')
bot = telebot.TeleBot(my_secret)


#help command functionality 
@bot.message_handler(commands = ['help','start'])
def greet(message):
  msg = ''' Available commmands:
  /greet will be replied with greet message
  /hello will send hello messsge
  Send /send_kitty to get a cat image.
  Send /eval expression to get the result of arithmetic operation for example /eval 5+7 '''
  bot.reply_to(message, msg)


@bot.message_handler(commands=["greet"])
def greet(message):
  bot.reply_to(message, "hey how are you , this is a greet from the bot")

@bot.message_handler(commands=["hello"])
def hello(message):
  bot.send_message(message.chat.id, "this is a hello from bot")


#command for arithmetic calculations
def val(message):
  if len(message.text.split()) > 2:
    return True

@bot.message_handler(commands=["eval"])
def calc(message):  
  re = message.text.strip("/eval")
  bot.reply_to(message, eval(re))

#example to fetch url from api and send image to user 
def get_kitty():
    contents = requests.get('https://api.thecatapi.com/v1/images/search').json()
    image_url = contents[0]['url']
    return image_url

@bot.message_handler(commands = ['send_kitty'])
def send_kitty(message):
    url = get_kitty()
    bot.send_message(message.chat.id, url)


bot.polling()
