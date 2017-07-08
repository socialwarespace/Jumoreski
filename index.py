#import config
import random
#import telebot
import loadAneks

#bot = telebot.TeleBot(config.TOKEN)

import config
import telebot
import os
from flask import Flask, request
bot = telebot.TeleBot(config.TOKEN)
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)

@bot.message_handler(content_types=["text"])
def send_anek(message):
    bot.send_message(message.chat.id, random.choice(loadAneks.aneks))



@server.route("/bot", methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=config.HOST)
    return "!", 200

server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
server = Flask(__name__)