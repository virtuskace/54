import telebot;
bot = telebot.TeleBot('5175757672:AAEbu8i1W5pYtuLcgxP4FjbFWELkmWXEujI');
@bot.message_handler(content_types=['text', 'document', 'audio'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "🔎 Для поиска отправьте код фильма/сериала");
    elif message.text == "хуй":
        bot.send_message(message.from_user.id, "1")
    elif message.text == "2":
        bot.send_message(message.from_user.id, "2")
    else:
        bot.send_message(message.from_user.id, "✖️ Код не найден! 🔎 Для поиска отправьте код фильма/сериала")
bot.polling(none_stop=True, interval=0)
