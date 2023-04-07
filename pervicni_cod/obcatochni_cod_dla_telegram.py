import string, json
# import requests
import logging
import time
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

# рабочий код
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["С пюрешкой", "Без пюрешки"]
    keyboard.add(*buttons)
    await message.answer("Как подавать котлеты?", reply_markup=keyboard)


sbor_input_2 = []
# рабочий код
@dp.message_handler(commands="polotno")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["матовое", "сатин","глянец"]
    keyboard.add(*buttons)
    await message.answer("Какок полтотно вы выберете?", reply_markup=keyboard)
    @dp.message_handler()  # func = lambda message: True)
    async def answer_to_user(message):
        global sbor_input_2
        sbor_input_2.append(message.text)
        print(message, sbor_input_2)


# обкат инлайн кнопок которые задают определеное действие

@dp.message_handler(commands="my_content")
async def cmd_inline_url(message: types.Message):
    # кнопки собираю в список
    buttons = [
        types.InlineKeyboardButton(text=" my GitHub", url="https://github.com/jeeand0305"),
        types.InlineKeyboardButton(text="Оф. канал Telegram", url="tg://resolve?domain=telegram")
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
