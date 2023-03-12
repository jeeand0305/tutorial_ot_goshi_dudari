from faile_config_telgr1 import * #open_weather_token
import requests
import telebot
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

# my_test_one_bot
TOKEN = "6224863591:AAGepg6cRgtv9wh0_Db17_sB_tfD81brgxA"


#____________________________________________________________
bot = Bot(TOKEN)
dp = Dispatcher(bot)

# понять что робот работает
async def on_startup(_):
    print("Bot is online")

# ______________________Клиентская часть-____________________
@dp.message_handlers(commands=['start', 'help'])
async def start_command(message:types.Message):
    try:
        await bot.send_message(\
            message.from_user.id, "Привет програмист")
        await message.delete()
    except:
        await message.reply("\
        Общение с ботом только в ЛС: \
        \n")




#natyznoy_potolok # назвапние бота
# @natyznoy_potolok_bot
# token_telegram =6063224285:AAF3eblLJGQiK9BWFtHyntaKRs7UdARASxQ
# natyznoy_potolok_grup0 # назвапние grup


bot = telebot.TeleBot\
    ("6224863591:AAGepg6cRgtv9wh0_Db17_sB_tfD81brgxA")\
    #(faile_config_telgr1.open_weather_token)

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
