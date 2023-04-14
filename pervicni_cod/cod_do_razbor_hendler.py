import string, json
import requests
import logging
import time
import test_obschet_poyolkov_bez_input
from aiogram import Bot, types, Dispatcher, executor
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

# from aiogram.utils import executor
# resurs
# https://mastergroosha.github.io/aiogram-2-guide/buttons/


# рабочий бот начала без разноса по директориям

TOKKEN = "6224863591:AAGepg6cRgtv9wh0_Db17_sB_tfD81brgxA"#my_test_bot
TOKEN="6063224285:AAF3eblLJGQiK9BWFtHyntaKRs7UdARASxQ"#natyznie potol
# natyznoy_potolok # назвапние бота
# @natyznoy_potolok_bot
# natyznoy_potolok_grup0 # назвапние grup

bot = Bot(TOKKEN)
dp = Dispatcher(bot)


async def on_startup(_):# палка в скобках решает
    print("bot v online")

# __________клиентская часть_____________
@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    try:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        batton_start ='ПОЕХАЛИИИИ'
        keyboard.add(batton_start)
        await message.answer("Здравствуйте 👋 меня зовут робот \
        Вася я предстовлю компанию СИОН", reply_markup=keyboard)
        await message.answer(" Жми ПОЕХАЛИИИИ я тебе все покажу")
    except:
        await message.reply(
            "Общение с ботом через ЛС, нпиши ему:\
            \nhttps://t.me/natyznoy_potolok_bot")



@dp.message_handler(lambda message: message.text == 'ПОЕХАЛИИИИ')
async def command_start(message : types.Message):
    try:
        key_batt = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_batt1 = 'Калькулятор потолка'
        key_batt2 = 'Режим работы'
        key_batt3 = 'Расположение'
        key_batt4 = 'Записаться на замер'
        key_batt.add(key_batt2, key_batt3).add(key_batt1, key_batt4)
        # reply_markup = keyboard прописывет что вывести перед надписью
        await message.answer('Главное меню', reply_markup=key_batt)
        # await message.delete()
    except:
        await message.reply(\
            "Общение с ботом через ЛС, нпиши ему:\
            \nhttps://t.me/natyznoy_potolok_bot")

request_u_users={
    1:"Прошу вас учесть данные нужно вводить в метрах пример\
     (14,23) метры можете не писать я вас и так пойму пиши ()",
    2:"Введи ширину комноты если нет пиши 0 :",
    3:"Введи длину комноты если нет пиши 0:",
    4:"Введи площадь комноты если нет пиши 0:",
    5:"Введи количество углов еcли нет пиши 0 :",
    6:"Введи количество труб ели нет пиши 0 :",
    7:"Введи количество светильников ели нет пиши 0 :",
    8:"Введи 1 если нужна наружная гардина на потолок или 0 если не надо :",
    9:"Ну и задали вы мне задачку схожжу посчитаю"
}

sbor_input_2 = []
# рабочий код
# Нужно доделать
# в случае ошибки при наборе просил позвонить в компанию для просчета
#  закинуть собранные данные на расчет
# ну и выдать просчет данных

@dp.message_handler(lambda message:message.text=='Калькулятор потолка')
async def cmd_start(message: types.Message):
    # try:
    global sbor_input_2
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["матовое", "сатин", "глянец"]
    keyboard.add(*buttons)
    await message.answer("Какок полтотно вы выберете?", reply_markup=keyboard)

# if len(sbor_input_2) < len(request_u_users):
@dp.message_handler(lambda message: message.text in ["матовое", "сатин","глянец"])
async def answer_to_user_polotno(message: types.Message):
    global sbor_input_2
    sbor_input_2.append(message.text)

    if len(sbor_input_2) < len(request_u_users) + 1:
        await message.answer(request_u_users[len(sbor_input_2)])
    @dp.message_handler(lambda message: message.text != None)
    async def answer_to_user_dlin(message: types.Message):
        global sbor_input_2
        sbor_input_2.append(message.text)
        if len(sbor_input_2) < len(request_u_users)+1:
           await message.answer(request_u_users[len(sbor_input_2)])
           print( sbor_input_2)
        if len(sbor_input_2) == 9:#len(request_u_users):
           # global sbor_input_2
           result_stoimosti_potolka={}
           # danie_na_oschet=[]
           print(sbor_input_2, "вторая проверка")
           danie_na_oschet = sbor_input_2
           dan_dict = test_obschet_poyolkov_bez_input.\
           poluchil_tuple_shirnu_dlinu_perim_ploshad(danie_na_oschet)
           price_poto_result = test_obschet_poyolkov_bez_input. \
               stoi_pot(dan_dict)
           if price_poto_result !=None:
               # price_gotovi="Стомость потолка без скидки ",price_poto_result[1],
               #              "cтомость потолка co скидкoй -15% ",price_poto_result[2]
               await message.answer(f"Стомость потолка без скидки {price_poto_result[1]}\
               cтомость потолка co скидкoй -15% {price_poto_result[2]}")
           sbor_input_2 = []



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
    key_return_v_osnovnoe_menu = types.InlineKeyboardButton \
        (text='Возврат в меню', callback_data='/start')
    key_batt_1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key_locat_req = types.KeyboardButton\
        (text='Отправить свою локацию 🗺️', request_location=True)
    key_conta_req = types.KeyboardButton\
        (text='Отправить свой контакт ☎️', request_contact=True)
    key_my_cont = 'Наши контакты'
    # key_return_v_osnovnoe_menu =types.InlineKeyboardButton\
    #     (text='Возврат в меню', callback_data='/start')
    key_batt_1.add(key_conta_req, key_locat_req)\
        .add(key_my_cont, key_return_v_osnovnoe_menu)
    # reply_markup = keyboard прописывет что вывести перед надписью
    await message.answer("Выберете вариант для связи",
                         reply_markup=key_batt_1)


# nado testit
@dp.message_handler(lambda message:message.text=='Наши контакты')
async def my_contakt (message: types.Message):
    await bot.send_message(message.from_user.id,
                           "Наши телефоны  8 982 118 63 83       8 904 833 47 57")

# Нужно отладить бота для возврат в главное меню
# @dp.message_handler(lambda message:message.text=='Возврат в меню')
# async def my_contakt (message: types.Message):
#     await bot.send_message(message.from_user.id, "/start")
#     await message.reply ("/start")
#     await message.delete()




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