# def benchmark(func):
#     import time
#
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         return_value = func(*args, **kwargs)
#         end = time.time()
#         print('[*] Время выполнения: {} секунд.'.format(end-start))
#         return return_value
#     return wrapper
#
# @benchmark
# def fetch_webpage(url):
#     import requests
#     webpage = requests.get(url)
#     return webpage.text
#
# webpage = fetch_webpage('https://google.com')
# print(webpage)
#
#






def decor_float_int(func):
    numb0_9=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    zapytaia = [',']
    type_danie=[float, int]
    def wraper(*args, **kwargs):
        # inaciliziruet function i beryt ie danie
        izm_1 = func(*args, **kwargs)
        izm_1= izm_1.replace(',','.')
        print(type(izm_1),izm_1)
        for i in izm_1:
            # print(i)
            if i in numb0_9:


                print(i)
                # print(izm_1, "print", type(izm_1))
        return izm_1
        # elif type(izm_1) != type_danie:
        #     for i in izm_1:
        #     print(izm_1, "print", type(izm_1))
        #     return izm_1
    return wraper


@decor_float_int
def izmer1():
    return input("Введи ширину комноты если нет пиши 0 : ")
shirina=izmer1()

# @decor_one
dlina = float(input("Введи длину комноты если нет пиши 0: "))

s_potolok = float(input("Введи площадь комноты если нет пиши 0:"))
ugol = int(input("Введи количество углов ели нет пиши 0 :"))
trub = int(input("Введи количество труб ели нет пиши 0 :"))
lite= int(input("Введи количество светильников ели нет пиши 0 :"))
# zaprose_dop_rabot=input("Дополнительные количество работ :")