import string, json
# import requests
import logging
import random
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

# старт бота прописыват что бот за работал
async def on_startup(_):# палка в скобках решает
    print("bot v online")


# Начальная кнопка катороя переносит в меню
@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    try:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        batton_start ='Меню'
        keyboard.add(batton_start)
        await message.answer("Здравствуйте 👋 меня зовут робот \
        Вася я предстовлю компанию СИОН", reply_markup=keyboard)
        await message.answer(" Жми 'Меню'я тебе все покажу")
    except:
        await message.reply(
            "Общение с ботом через ЛС, нпиши ему:\
            \nhttps://t.me/natyznoy_potolok_bot")


# открывает кнопки главного меню который отлавливается\
# через лянду
@dp.message_handler(lambda message: message.text == 'Меню')
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

# текст для запросов может лучше сделать на один из модуль пока так
request_u_users = {
    1:"Прошу вас учесть данные нужно вводить в метрах пример\
     (1,3) метры можете не писать я вас и так пойму пиши \
     понял пиши 1 нет 0",
    2:"Введи ширину комноты если не знаете пишите 0 :",
    3:"Введи длину комноты если не знаете пишите 0:",
    4:"Введи площадь комноты если ввели ширину и длину пишите 0:",
    5:"Введи количество углов еcли нет пиши 0 :",
    6:"Введи количество труб ели нет пиши 0 :",
    7:"Введи количество светильников ели нет пиши 0 :",
    8:"Введи 1 если нужна наружная гардина на потолок или 0 если не надо :",
    9:"Ну и задали вы мне задачку схожжу посчитаю"
}


sbor_input_2 = []
# запуск калькулятор и делает просчет с модуля \
# test_obschet_poyolkov_bez_input \
# очень часто вылетел сечас роботал
@dp.message_handler(lambda message:message.text=="Калькулятор потолка")
async def cmd_start(message: types.Message):
    global sbor_input_2
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["матовое", "сатин", "глянец"]
    battons_menu = [ 'Меню' ]
    keyboard.add(*buttons).add(*battons_menu)
    await message.answer("Выберет полотно если хотите расчитать\
     стоимость вашего потолка или 'Меню' для возврата\
      в главное меню ",\
                         reply_markup=keyboard)

#отлавливает наименование полотна и запускает пербор запросов
@dp.message_handler(lambda message: message.text in ["матовое", "сатин","глянец"])
async def answer_to_user_polotno(message):
    global sbor_input_2
    sbor_input_2.append(message.text)
    if len(sbor_input_2) < len(request_u_users) + 1:
        await message.answer(request_u_users[len(sbor_input_2)])
    # собирает все что вы вводите и список полученные данные
    # переписать чтобы исключить сбор всех даных которые \
    # не явлются цифрой или запятой
    @dp.message_handler(lambda message: message.text != None)
    async def answer_to_user_dlin(message):
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


@dp.message_handler(Text(equals='Режим работы'))
async def sion_open_command(message : types.Message):
    await bot.send_message(
        message.from_user.id, " Ежедневно с9-00 до \
21-00 без Выходных")


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
        (text='Отправить свою локацию 🗺️', request_location=True)
    key_conta_req = types.KeyboardButton\
        (text='Отправить свой контакт ☎️', request_contact=True)
    key_return_v_osnovnoe_menu = 'Меню'
    key_my_online = 'Как нас найти в интернете'
    key_my_cont = 'Наши контакты'
    key_batt_1.add(key_conta_req, key_locat_req)\
        .add(key_my_cont, key_my_online)\
        .add(key_return_v_osnovnoe_menu)
    # reply_markup = keyboard прописывет что вывести перед надписью
    await message.answer("Выберете вариант для связи",
                         reply_markup=key_batt_1)

@dp.message_handler(lambda message:message.text=='Наши контакты')
async def my_contakt (message: types.Message):
    await bot.send_message(message.from_user.id,\
        "Наши телефоны  8 982 118 63 83  8 904 833 47 57")


@dp.message_handler(lambda message: \
                message.text=='Как нас найти в интернете')
async def cmd_inline_url(message: types.Message):
    # кнопки собираю в список
    buttons = [
        types.InlineKeyboardButton(text="Мы в Контакте",\
            url="https://vk.com/clubsion18"),
        types.InlineKeyboardButton(text="Наш сайт",\
            url="http://sion18.ru/")
    ]
    # Задает ширину строки (row_width=1)
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    # Заносим в переменную keyboard кнопки где .add означает
    # друг под другом, *buttons со зездочкой потому что как
    # *args. **kwargs
    keyboard.add(*buttons)
    await message.answer("Кнопки-ссылки", reply_markup=keyboard)

# предворительно пишу калькулятор для понимания работ и логики
value = ''
old_value = ''

@dp.message_handler(commands="calculator")
async def cmd_inline_url(message: types.Message):
    # кнопки собираю в список
    buttons = [
        types.InlineKeyboardButton(text="<-",\
                callback_data=" "),
        types.InlineKeyboardButton(text=" ",\
                callback_data="no"),
        types.InlineKeyboardButton(text="C", \
                callback_data="_"),
        types.InlineKeyboardButton(text="+/-", \
                callback_data="-1")
    ]
    buttons2 = [
        types.InlineKeyboardButton(text="7",\
                callback_data="7"),
        types.InlineKeyboardButton(text="8",\
                callback_data="8"),
        types.InlineKeyboardButton(text="9", \
                callback_data="9"),
        types.InlineKeyboardButton(text="/", \
                callback_data="/")
    ]
    buttons3 = [
        types.InlineKeyboardButton(text="4", \
                callback_data="4"),
        types.InlineKeyboardButton(text="5", \
                callback_data="5"),
        types.InlineKeyboardButton(text="6", \
                callback_data="6"),
        types.InlineKeyboardButton(text="*", \
                callback_data="*")
    ]
    buttons4 = [
        types.InlineKeyboardButton(text="1", \
                                   callback_data="1"),
        types.InlineKeyboardButton(text="2", \
                                   callback_data="2"),
        types.InlineKeyboardButton(text="3", \
                                   callback_data="3"),
        types.InlineKeyboardButton(text="-", \
                                   callback_data="-")
    ]
    buttons5 = [
        types.InlineKeyboardButton(text="0", \
                                   callback_data="0"),
        types.InlineKeyboardButton(text=",", \
                                   callback_data="."),
        types.InlineKeyboardButton(text="+", \
                                   callback_data="+"),
        types.InlineKeyboardButton(text="=", \
                                   callback_data="=")
    ]

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.row(*buttons).row(*buttons2).row(*buttons3)\
        .row(*buttons4).row(*buttons5)
    await message.answer("калькулятор", reply_markup=keyboard)


@dp.message_handler(commands=['text'])
async def get_messange(message):
    global value
    if value == '':
        bot.send_message(message.from_user.id, '0', reply_markup='keyboard')
    else:
        bot.send_message(message.from_user.id, value, reply_markup='keyboard')


@dp.message_handler(commands="random")
async def cmd_random(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Нажми меня", callback_data="random_value"))
    await message.answer("Нажмите на кнопку, чтобы бот отправил число от 1 до 10", reply_markup=keyboard)



@dp.callback_query_handler(text="random_value")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(str(random.randint(1, 10)))
# @dp.

# @dp.callback_query_handler(func=lambda call: True)
# async def analis_danih_s_calculator(query):
#     global value, old_value
#     date= query.date
#     if date == "no":
#         pass
#     elif date == 'C':
#         value =''
#     elif date == '=':
#         value = str(eval(value))
#     else:
#         value+=date
#
#     if value != old_value:
#         if value=='':
#             bot.edit_message_text(chat_id=query.message.chat.id, \
#             message_id=query.massage.id, text='0', reply_markup='keyboard')
#         else:
#             bot.edit_message_text(chat_id=query.message.chat.id,\
#             message_id=query.massage.id, text=value,reply_markup='keyboard')
#     old_value = value

# if __name__ == '__main__':
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
