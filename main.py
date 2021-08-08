from telebot import TeleBot, types
import config
# import sqlite3

bot = TeleBot(config.TOKEN)


# def id_adder(message):
#     connect = sqlite3.connect('users.db')
#     cursor = connect.cursor()
#     cursor.execute("""CREATE TABLE IF NOT EXISTS users_id(
#                     id INTEGER
#                 )""")
#     connect.commit()
#
#     cursor.execute(f"SELECT id FROM users_id WHERE id = {message.chat.id}")
#     data = cursor.fetchone()
#     if data is None:
#         user_id = [message.chat.id]
#         cursor.execute("INSERT INTO users_id VALUES(?);", user_id)
#     connect.commit()


@bot.message_handler(commands=['start'])
def start(message):
    # id_adder(message)

    bot.send_message(message.chat.id, "Этот бот рофлит над челиками. Ответь на сообщение /roflan и сам все увидишь",
                     reply_markup=types.ForceReply())


@bot.message_handler(commands=['roflan'])
def humor(message):
    try:
        # id_adder(message)

        text = message.reply_to_message.text.lower()
        text = list(text)
        for symbol_index in range(len(text)):
            if symbol_index % 2 != 0:
                symbol = text[symbol_index]
                text[symbol_index] = symbol.upper()
        bot.reply_to(message.reply_to_message, ''.join(text))
    except:
        pass


bot.set_my_commands([types.BotCommand("/start", "старт"), types.BotCommand("/roflan", "зарофлить")])

if __name__ == '__main__':
    bot.polling(none_stop=True)
