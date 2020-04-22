# телеграм бот советчик по погоде
import pyowm
import telebot

owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc', language="ru")  # You MUST provide a valid API keyщць = знщцьюЩЦЬ(э6в00в1в4у704068в70191ифв2673у0ссэ)  № Нщг ЬГЫЕ зкщмшву ф мфдшв ФЗШ лун

bot = telebot.TeleBot('1292667823:AAHQ9osRe8tl5afJIz0N_YjvkOYcJlo5aWI')

@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place(message.text)
	w = observation.get_weather()
	temp = w.get_temperature('celsius') ["temp"]


	answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + "\n"
	answer += "Температура сейчас в районе " + str(temp) + "\n\n"

	if temp < 10:
		answer += " Сейчас писец как холодно, одевайся теплее"
	elif temp < 20:
		answer += " Сейчас холодно, одевайся норм"
	else:
		answer += " Температура норм, можешь не одеваться"

    bot.send_message(message.chat.id, answer)
 
bot.polling(none_stop = True)
