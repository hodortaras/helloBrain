import telebot
import os

bot = telebot.TeleBot("862733109:AAHaIObuRsswV7gvNfMjiBzS0nmetHNahwY")

@bot.message_handler(commands=['test'])
def find_file_ids(message):
    for file in os.listdir('music/'):
        if file.split('.')[-1] == 'mp3':
            f = open('music/'+file, 'rb')
            msg = bot.send_audio(message.chat.id, f)
            # А теперь отправим вслед за файлом его file_id
            bot.send_audio(message.chat.id, msg, reply_to_message_id=msg.message_id)
        time.sleep(15)


if __name__ == '__main__':
    bot.polling(none_stop=True)
