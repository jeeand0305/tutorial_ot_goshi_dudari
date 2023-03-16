import asyncio
import string
import json

# types={1:"Привет сука", 2:"Привет сучка"}
types="Привет"
# types=["Привет сука"]

# file_json = (open("cenz.json","r", encoding="cp1251"))
# file_json = (open("cenz.json","r", encoding="utf-8"))
# print(file_json.read())


async def echo_send(message=types):
    # for i in message.lower().split(' '):
    #     print(i)
    #     # if i.lower()
   if {i.lower().translate(str.maketrans
    ('', '', string.punctuation))
    for i in message.split(' ')}.intersection(set
    (json.load(open('cenz.json')))) != set():
       message="мат запрещен"
       print(message)
       # message.delite()

async def main():
    print('Hello ...')

    await asyncio.sleep(1)
    await echo_send(types)
    print('... World!')

asyncio.run(main())



       # orignl
       # async def echo_send(message: types.Message):
       #    if {i.lower().translate(str.maketrans
       #     ('', '', string.punctuation))
       #     for i in message.text.split(' ')}.intersection(set
       #     (json.load(open('cenz.json')))) != set():
       #        await message.reply("мат запрещен")
       #        await message.delite()
