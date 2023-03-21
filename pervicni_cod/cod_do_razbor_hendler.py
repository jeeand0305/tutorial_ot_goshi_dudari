import string, json
import requests
import logging
import time
from aiogram import Bot, types, Dispatcher, executor
from aiogram.dispatcher.filters import Text
# from aiogram.utils import executor
# resurs
# https://mastergroosha.github.io/aiogram-2-guide/buttons/


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
@dp.message_handler(commands=['start'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id,\
                               'Здравствуйте рад буду помочь')
        async def keybord_bot(message: types.Message):
            key_batt = types.ReplyKeyboardMarkup(resize_keyboard=True)
            key_batt1 = 'Калькулятор потолка'
            key_batt2 = 'Режим работы'
            key_batt3 = 'Расположение'
            key_batt4 = 'Записаться на замер'
            key_batt.add(key_batt2, key_batt3).add(key_batt1, key_batt4)
            # reply_markup = keyboard прописывет что вывести перед надписью
            await message.answer("Какой потолок вас инетересует?", \
                                 reply_markup=key_batt)
        await message.delete()
    except:
        await message.reply(\
            "Общение с ботом через ЛС, нпиши ему:\
            \nhttps://t.me/natyznoy_potolok_bot")



# otlov poluchenih zaprosov
# отлавливает нажатие кнопки через модуль в питоне\
# (Text(equals='Режим работы'))
@dp.message_handler(Text(equals='Режим работы'))
async def sion_open_command(message : types.Message):
    await bot.send_message(
        message.from_user.id, " Ежедневно с9-00 до \
21-00 без Выходных")


# отлавливает нажатие кнопки через lambda message: message.text
@dp.message_handler(lambda message: message.text=='Расположение')
async def sion_place_command(message : types.Message):
    await bot.send_message(
        message.from_user.id,\
        "ТЦ Азбука ремонта и ТЦ Гвоздь")


@dp.message_handler(lambda message:\
                            message.text=='Записаться на замер')
async def key_sett_zamer(message: types.Message):
    key_batt_1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key_locat_req = types.KeyboardButton\
        (text='Запросить геолакацию', request_location=True)
    key_conta_req = types.KeyboardButton\
        (text= 'Запросить контакт', request_contact=True)
    key_my_cont = 'Наши контакты'
    key_batt_1.add(key_conta_req, key_locat_req).add(key_my_cont)
    # reply_markup = keyboard прописывет что вывести перед надписью
    await message.answer("Выберете вариант для связи", \
                         reply_markup=key_batt_1)

# nado testit
# async def my_contakt (lambda message:message.text=='Наши контакты'):
#     await bot.send_message(message.from_user.id,\
#         "Наши телефоны / 8 982 118 63 83 / 8 904 833 47 57")




# отлов мата
@dp.message_handler()
async def echo_send(message: types.Message):
    if {i.lower().translate(str.maketrans
    ('', '', string.punctuation))
    for i in message.text.split(' ')}.intersection(set
    (json.load(open('cenz.json')))) != set():
       await message.reply("мат запрещен")
       await message.delete()






executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

# airogram rabochi cod
# @dp.message_handler()
# async def echo_send(message: types.Message):
    # просто эхо что написал то и получил обратно
    #await message.answer(message.text)
    # эхо и но при этом прописывает имя пользовотеля
    # await message.reply(message.text)
    # если бот в групе отвечает тебе в личку
    #await bot.send_message(message.from_user.id, message.text)

# @dp.message_handler(commands="start")
# async def cmd_start(message: types.Message):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     buttons = ["Матовый потолок", "Глянцевый потолок"]
#     keyboard.add(*buttons)
#     await message.answer("Какой потолок вас инетересует", reply_markup=keyboard)

# work cod
# @dp.message_handler(commands='калькулятор потолка')
# async def vari_polotna(message: types.Message):
#     # resize_keyboard=True прописывает размер кнопок\
#     # и зарезервировал переменую
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     # нименование кнопок
#     polotno = "Матовый потолок"
#     glanec_polo = "Глянцевый потолок"
#     # присвоение назвние кнопок
#     # .add в один ряд
#     # .input присоеденить в ширину
#     keyboard.add(polotno, glanec_polo)
#     # reply_markup = keyboard прописывет что вывести перед надписью
#     await message.answer("Какой потолок вас инетересует?", reply_markup=keyboard)
#
# work cod
# @dp.message_handler(commands=["Режим работы"])
# async def sion_open_command(message : types.Message):
#     await bot.send_message(
#         message.from_user.id, " Ежедневно с9-00 до \
# 21-00 без Выходных")

# keybord is bot work
# @dp.message_handler(Text(equals='start'))
# async def keybord_bot(message: types.Message):
#     key_batt = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     key_batt1 = 'Калькулятор потолка'
#     key_batt2 = 'Режим работы'
#     key_batt3 = 'Расположение'
#     key_batt4 = 'Записаться на замер'
#     key_batt.add(key_batt2, key_batt3).add(key_batt1, key_batt4)
#     # reply_markup = keyboard прописывет что вывести перед надписью
#     await message.answer("Какой потолок вас инетересует?",\
#                          reply_markup=key_batt)