from create_bot import dp
from aiogram.utils import executor
# from hedlers import client, admin, other
import client, other
# from create_bot import dp, bot


async def on_startup(_):# палка в скобках решает
    print("bot v online")



client.register_hedler_client(dp)
other.register_hedler_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)