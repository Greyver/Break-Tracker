import time
import telebot

# Вставьте свой токен
TOKEN = '7907059765:AAH4VAYMStd6TuKW959hbqwO4KQysptJ2sA'
CHAT_ID = '-4582182912'

bot = telebot.TeleBot(TOKEN)

def send_periodic_message():
    while True:
        bot.send_message(CHAT_ID, "Топовые рабовладельцы: @Zero_Deus, @ghstfld, @Syperion")
        time.sleep(16200)  # Задержка в 120 секунд (2 минуты)

# Запускаем функцию отправки сообщений в бесконечном цикле
if __name__ == "__main__":
    send_periodic_message()
