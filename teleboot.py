import telebot
import pyowm

bot = telebot.TeleBot("862733109:AAHaIObuRsswV7gvNfMjiBzS0nmetHNahwY")
owm = pyowm.OWM('c43f219f19f3c91f06a9929b446f7837', language = "ru" )  # You MUST provide a valid API key

@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = owm.weather_at_place(message.text)
    w = observation.get_weather()
    temp = w.get_temperature('celsius') ["temp"]

    answer ="В городе " + message.text + " погода сейчас " + w.get_detailed_status() + "\n"
    answer +="Температура сейчас в районе " + str(temp) + "\n\n"
    if temp <10:
        answer +="Дубарь, оденься потеплее!!!"
    elif temp<20:
        answer +="Прохладно, время весенней куртки!"
    elif temp>20:
        answer +="Вперед тусить, шорты и футболка)))"


    bot.send_message(message.chat.id, answer)
    #bot.reply_to(message, message.text)

bot.polling( none_stop = True )
