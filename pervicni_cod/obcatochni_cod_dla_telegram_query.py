import telebot, datetime, time, math, re
from aiogram import Bot, types, Dispatcher, executor
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from telebot import types

TOKKEN = "6224863591:AAGepg6cRgtv9wh0_Db17_sB_tfD81brgxA"#my_test_bot
TOKEN="6063224285:AAF3eblLJGQiK9BWFtHyntaKRs7UdARASxQ"#natyznie potol

BOT_NAME = 'calc_bot' # Имя для бота. Нужно в том случае, если вы хотите обращаться к боту по имени
bot = telebot.TeleBot(TOKEN)

bot = Bot(TOKKEN)
dp = Dispatcher(bot)

TIMEOUT_CONNECTION = 5 # Таймаут переподключения

# собирает данные в глобальную переменую на модуле телебот
# или надо полученные данные еще обробатывать убирать /
# запятые итому подобное это придется делать через еще/
# один дополнилельный декоратор

# @dp.message_handler(commands="start")
# async def cmd_start(message: types.Message):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     buttons = ["С пюрешкой", "Без пюрешки"]
#     keyboard.add(*buttons)
#     await message.answer("Как подавать котлеты?", reply_markup=keyboard)
#
# @dp.message_handler(commands="test1")
# async def cmd_test1(message: types.Message):
#     await message.reply("Test 1")




sbor_input_2=[]
# @bot.message_handler(func = lambda message: True)
# получилось собратьть данные тоько для модуля телеблот
@dp.message_handler()#func = lambda message: True)
async def answer_to_user(message):
    global sbor_input_2
    sbor_input_2.append(message.text)
    print(message, sbor_input_2)

# задачи
# 1. сделать так чтобы телеграм задавл вопросы друг другом
# желательно кнопокоми
# 2. мы собирали данные ответов с того что собирал телеграм
# 3.Данные закинули листом в программу обсчет потолка
# 4.полученный ответ отапрвмли в телеграмм



#
# # cod is chuizogo git hube
# # Обработчик inline-запроса
# @bot.inline_handler(func=lambda query: True)
# def inline_answer_to_user(inline_query):
#     print(inline_query,bot )
#     answer = 0
#     answer_list = []
#     try:
#         answer = str(eval(inline_query.query.lower().replace(' ', '')))
#         answer_to_send = answer.replace('*', '\*')
#         query_to_send = inline_query.query.replace('*', '\*').lower().replace(' ', '')
#
#         answer_list.append(types.InlineQueryResultArticle(
#             id=0,
#             title='Отправить с выражением',
#             description='%s = %s' % (inline_query.query, answer),
#             input_message_content=types.InputTextMessageContent(
#                 message_text='%s = *%s*' % (query_to_send, answer_to_send),
#                 parse_mode='markdown'),
#
#         ))
#
#         answer_list.append(types.InlineQueryResultArticle(
#             id=1,
#             title='Отправить без выражения',
#             description='%s' % (answer),
#             input_message_content=types.InputTextMessageContent(
#                 message_text='*%s*' % (answer_to_send),
#                 parse_mode='markdown'),
#
#         ))
#
#     except SyntaxError:
#         answer = False
#     except NameError:
#         answer = False
#     except TypeError:
#         answer = False
#     except ZeroDivisionError:
#         answer = False
#
#     if (not answer):
#         answer_list = []
#         answer_list.append(types.InlineQueryResultArticle(
#             id=0,
#             title='Калькулятор',
#             description='Чтобы посичтать выражение - введите его.\
#             nЕсли вы хотите просмотреть справку, то перейдите в диалог со мной и напишите \"/help\"',
#             input_message_content=types.InputTextMessageContent(
#                 message_text='Я хотел посчитать выражение, но нажал не туда')
#         ))
#
#     bot.answer_inline_query(inline_query.id, answer_list)
#

# # cod is
# # @dp.callback_query_handler(func=lambda call: True)
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

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    # while True:
    #     try:
    #         bot.polling(none_stop=True)
    #     except Exception as e:
    #         print ('Ошибка подключения. Попытка подключения через %s сек.'%TIMEOUT_CONNECTION)
    #         time.sleep(TIMEOUT_CONNECTION)