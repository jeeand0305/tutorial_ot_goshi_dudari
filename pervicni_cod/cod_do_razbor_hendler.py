import string, json
import requests
import telebot
import logging
import time
from aiogram import Bot, types, Dispatcher, executor
# from aiogram.dispatcher import Dispatcher
# from aiogram.utils import executor
from keybord_2 import kb_client


# рабочий бот начала без разноса по директориям

TOKKEN = "6224863591:AAGepg6cRgtv9wh0_Db17_sB_tfD81brgxA"
TOKEN="6063224285:AAF3eblLJGQiK9BWFtHyntaKRs7UdARASxQ"
# natyznoy_potolok # назвапние бота
# @natyznoy_potolok_bot
# natyznoy_potolok_grup0 # назвапние grup

bot = Bot(TOKKEN)
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

# отлов мата
@dp.message_handler()
async def echo_send(message: types.Message):
    if {i.lower().translate(str.maketrans
    ('', '', string.punctuation))
    for i in message.text.split(' ')}.intersection(set
    (json.load(open('cenz.json')))) != set():
       await message.reply("мат запрещен")
       await message.delete()



def register_messenger(dp: Dispatcher):
    dp.register_message_handler\
        (sion_open_command, commands=["Режим_работы"])
    dp.register_message_handler\
        (sion_place_command, commands=["Расположение"])

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