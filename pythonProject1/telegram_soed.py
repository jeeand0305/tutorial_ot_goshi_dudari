import requests
import telebot
import logging
import time
from aiogram import Bot, types, Dispatcher, executor
# from aiogram.dispatcher import Dispatcher
# from aiogram.utils import executor


# _рабочий код пишет эхо + suka_________________________________
# bot = telebot.TeleBot\
#     ("6224863591:AAGepg6cRgtv9wh0_Db17_sB_tfD81brgxA")#(faile_config_telgr1.open_weather_token)
#
# @bot.message_handler(content_types=["text"])
# def eho_test(messag):
#     bot.send_message(messag.chat.id, messag.text+" suka")
#
# bot.polling(none_stop =True)
# _________________________________________


#  бот на погоду не работает апи ошибка____________
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


# xz no work _______________________________________
# def  telegram_bot(open_weather_telegram):
#     bot = telebot.TeleBot(open_weather_telegram)
#
#     @bot.message_handlers(commands=["start"])
#     def start_message(massage):
#         bot.send_message(message.chat.id, \
#         "Hello friend")
# ______________________________________________
# def main():
#     city = input("Введите город: ")
#     get_weather(city, open_weather_token)

# #probnik po zapusku telegram bota

# ____________________________________________________________


# не работает __________________________________
# MSG= "Програмировал ли ты сегодня , {} ???"
# TOKKEN = "6224863591:AAGepg6cRgtv9wh0_Db17_sB_tfD81brgxA"
#
# bot = Bot(token=TOKKEN)
# dp = Dispatcher(bot=bot)
#
# @dp.messa

# @dp.message_handlers(commands=["start"])
# async def start_command(message:types.Message):
#     await message.reply("Привет програмист ")e
#


# async def start_handlera(message:types.Message):
#     user_id = message.from_user.id
#     user_name = message.from_user.first_name
#     user_full_name = message.from_useer.full_name
#     logging.info(f'{user_id=} {user_full_name=}\
#     .time.asctime()')
#     await message.replay\
#         (f"Привет мартышка, {user_full_name}")
#
#     for i in range(10):
#         time.sleep(2)
#         await bot.send_message(user_id, \
#                                MSG.format(user_name))
#
# if __name__ == '__main__':
#     executor.start_polling(dp)

#
# TOKKEN = "6224863591:AAGepg6cRgtv9wh0_Db17_sB_tfD81brgxA"
#
# bot = Bot(token=TOKKEN)
# dp = Dispatcher(bot=bot)
#
# @dp.message_handler(commands=["start"])
# async def st_com(message:types.Message):
#     await message.reply("help im ")
#
# if __name__ == '__main__':
#     executor.start_polling(dp)

TOKEN="6063224285:AAF3eblLJGQiK9BWFtHyntaKRs7UdARASxQ"
# natyznoy_potolok # назвапние бота
# @natyznoy_potolok_bot
# natyznoy_potolok_grup0 # назвапние grup

bot = Bot(TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):# палка в скобках решает
    print("bot v online")
# __________клиентская часть_____________
@dp.message_handler(commands=['start','help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Отличных покупок')
        await message.delete()
    except:
        await message.reply(\
            "Общение с ботом через ЛС, нпиши ему:\
            \nhttps://t.me/natyznoy_potolok_bot")
@dp.message_handler(commands=["Режим_работы"])
async def sion_open_command(message : types.Message):
    await bot.send_message(
        message.from_user.id, " Ежедневно с9-00 до \
21-00 без Выходных")

@dp.message_handler(commands=["Расположение"])
async def sion_place_command(message : types.Message):
    await bot.send_message(
        message.from_user.id,\
        "ТЦ Азбука ремонта и ТЦ Гвоздь")



# __________админская часть _____________
# __________общая частть _________-___

@dp.message_handler()
async def echo_send(message: types.Message):
   if message.text != "h":
       await message.answer("И тебе "+ message.text)



# airogram rabochi cod
# @dp.message_handler()
# async def echo_send(message: types.Message):
    # просто эхо что написал то и получил обратно
    #await message.answer(message.text)
    # эхо и но при этом прописывает имя пользовотеля
    # await message.reply(message.text)
    # если бот в групе отвечает тебе в личку
    #await bot.send_message(message.from_user.id, message.text)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)