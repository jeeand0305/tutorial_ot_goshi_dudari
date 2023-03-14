
import telebot


# my_test_one_bot
TOKEN = "6224863591:AAGepg6cRgtv9wh0_Db17_sB_tfD81brgxA"


#____________________________________________________________


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
