import telebot

bot = telebot.TeleBot("862733109:AAHaIObuRsswV7gvNfMjiBzS0nmetHNahwY")

@bot.message_handler(content_types=["text"])
def repeet(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.polling(none_stop=True)
