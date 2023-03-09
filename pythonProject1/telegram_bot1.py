from faile_config_telgr1 import * #open_weather_token
import requests
import telebot
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

# my_test_one_bot


# def get_weather(city, open_weather_token ):
#     try:
#         r=requests.get(
#             f"http://api.openweathermap.org/geo/1.0/direct?q=\
# {city}&appid= \
# {open_weather_token}"
#         )
#         data = r.json()
#         print(data)
#     # {city name}, {state code}, {country code}
#     except Exception as ex:
#         print(ex)
#         print("Prover name city")

# xz no work
# def  telegram_bot(open_weather_telegram):
#     bot = telebot.TeleBot(open_weather_telegram)
#
#     @bot.message_handlers(commands=["start"])
#     def start_message(massage):
#         bot.send_message(message.chat.id, "Hello friend")

# ______________________________________________
# def main():
#     city = input("Введите город: ")
#     get_weather(city, open_weather_token)

# #probnik po zapusku telegram bota

# ____________________________________________________________
# bot = Bot(token=open_weather_telegram)
# dp = Dispatcher(bot)
#
# @dp.message_handlers(commands=["start"])
# async def start_command(message:types.Message):
#     await message.reply("Привет програмист ")e
#

#natyznoy_potolok # назвапние бота
# @natyznoy_potolok_bot
# token_telegram =6063224285:AAF3eblLJGQiK9BWFtHyntaKRs7UdARASxQ
# natyznoy_potolok_grup0 # назвапние grup


bot = telebot.TeleBot\
    ("6224863591:AAGepg6cRgtv9wh0_Db17_sB_tfD81brgxA")#(faile_config_telgr1.open_weather_token)

@bot.message_handler(content_types=["text"])
def eho_test(messag):
    bot.send_message(messag.chat.id, messag.text * 6  )# + " hello im popugay"

bot.polling(none_stop =True)


# if __name__ == '__main__':

    # executor.start_polling(dp)
    # telegram_bot(open_weather_telegram)



# my_test_one_bot
# my_test_tutorial_bot
# token = 6224863591:AAGepg6cRgtv9wh0_Db17_sB_tfD81brgxA
