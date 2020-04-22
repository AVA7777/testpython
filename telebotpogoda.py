# телеграм бот советчик по погоде

import telebot

from telebot import apihelper

apihelper.proxy = {'http':'http://10.10.1.10:3128'}

bot = telebot.TeleBot('1292667823:AAHQ9osRe8tl5afJIz0N_YjvkOYcJlo5aWI')

@bot.message_handler(content_types=['text'])
def echo_message(message):
    bot.send_message(message.chat.id, message.text)
 
bot.polling(none_stop = True)
