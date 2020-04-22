# телеграм бот советчик по погоде

import telebot

bot = telebot.TeleBot('1292667823:AAHQ9osRe8tl5afJIz0N_YjvkOYcJlo5aWI')

@bot.message_handler(content_types=['text'])
def send_echo(message):
    bot.send_message(message.chat.id, message.text)
 
bot.polling(none_stop = True)
