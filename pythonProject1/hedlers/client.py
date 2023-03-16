from aiogram import types, Dispatcher
import os
from create_bot import dp, bot



# @dp.message_handler(commands=['start','help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message\
            (message.from_user.id, 'Отличных покупок')
        await message.delete()
    except:
        await message.reply
        ("Общение с ботом через ЛС, нпиши "
         "ему:\nhttps://t.me/natyznoy_potolok_bot")

# @dp.message_handler(commands=["Режим_работы"])
async def sion_open_command(message : types.Message):
    await bot.send_message(
        message.from_user.id, " Ежедневно с9-00 до \
21-00 без Выходных")

# @dp.message_handler(commands=["Расположение"])
async def sion_place_command(message : types.Message):
    await bot.send_message(
        message.from_user.id,\
        "ТЦ Азбука ремонта и ТЦ Гвоздь")



def register_hedler_client(dp: Dispatcher):
   dp.register_message_hedler\
       (command_start, commands=['start', 'help'])
   dp.register_message_hedler\
       (sion_open_command, commands=["Режим_работы"])
   dp.register_message_hedler\
       (sion_place_command, commands=["Расположение"])
