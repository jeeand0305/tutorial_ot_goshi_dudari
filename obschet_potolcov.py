
price = {"PK": 2100, "baget": 150, "polotnoMDS_320":210 ,
    "polotnoMDS_3.6": 380, "polotnoMDS_4-5": 410, "premium_3.6": 390,
    "premium_5": 480, "NO": 500,
    "lamp": 350, "BL": 1000, "vstavka": 90, "ugol": 60, "truba_st": 350,
    "brus_al": 300
}
list_otbora=['1','2','3','4','5','6','7','8','9','0', '.']

def decor_float_int(func):
    def wrapper(*args, **kwargs):
        loc_str=''
        # inaciliziruet function i beryt ie danie
        izm_1 = func(*args, **kwargs)
        izm_1 = izm_1.replace(',', '.').lower()
        if izm_1[0] in '.':
            del izm_1[0]
        for izm_1_one in izm_1:
            if izm_1_one in list_otbora:
                loc_str +=izm_1_one
            # elif izm_1_one not in list_otbora:
            #     loc_str='0lkj'
            #     print(loc_str, 'hello2')
        # print(loc_str, 'posled')
        loc_str = (lambda loc_str: loc_str[1:] if loc_str[0] == '.' else loc_str)(loc_str)
        # print(loc_str, "hello1")
        return float(loc_str)
    return wrapper


@decor_float_int
def marca_polotna():
    return input("выбери потлотно нажми цифру classic-1, premium-2, evoliyion-3 : ")

shirina = marca_polotna()

@decor_float_int
def izmer1():
    return input("Введи ширину комноты если нет пиши 0 : ")

shirina = izmer1()


@decor_float_int
def izmer2():
    return input("Введи длину комноты если нет пиши 0: ")

dlina = izmer2()


@decor_float_int
def izmer3():
    return input("Введи площадь комноты если нет пиши 0:")

s_potolok = izmer3()


@decor_float_int
def izmer4():
    return input("Введи количество углов еcли нет пиши 0 :")

ugol = izmer4()


@decor_float_int
def izmer5():
    return input("Введи количество труб ели нет пиши 0 :")

trub = izmer5()


@decor_float_int
def izmer6():
    return input("Введи количество светильников ели нет пиши 0 :")

lite = izmer6()

@decor_float_int
def izmer7():
    return input("Введи 1  если нужна наружная гардина на потолок или 0 если не надо :")

brus = izmer7()


# print(zaprose_dop_rabot)

def poluchil_tuple_shirnu_dlinu_perim_ploshad():
    dlina_f = dlina
    shirina_f = shirina
    s_potolok_f = s_potolok
    ugol_f = ugol
    trub_f = trub
    lite_f = lite
    perimetr_f=0
    shi_dli_per_plo = {}
    if shirina_f > 0 and dlina_f > 0:
        s_potolok_f = dlina_f*shirina_f
        perimetr_f = (dlina_f+shirina_f)*2
        # замена ширины и длины между собой
        if dlina_f <= shirina_f:
            dlina_f, shirina_f = shirina_f, dlina_f
    elif shirina_f > 0 and s_potolok_f:#>0 or dlina > 0:
        dlina_f = s_potolok_f / shirina_f
        perimetr_f = (dlina_f+shirina_f)*2
        if dlina_f < shirina_f:
            dlina_f, shirina_f = shirina_f, dlina_f
    elif dlina_f > 0 and s_potolok_f:#>0 or :
        shirina_f = s_potolok_f / dlina_f
        perimetr_f = (dlina_f+shirina_f)*2
        if dlina_f < shirina_f:
            dlina_f, shirina_f = shirina_f, dlina_f
    elif shirina > 0 and dlina > 0 or s_potolok>0:
        dlina_f = 4
        shirina_f = s_potolok_f / dlina_f
        perimetr_f = (dlina_f + shirina_f) * 2
        if dlina_f < shirina_f:
            dlina_f, shirina_f = shirina_f, dlina_f

    shi_dli_per_plo['shirina_f'] = shirina_f
    shi_dli_per_plo['dlina_f'] = dlina_f
    shi_dli_per_plo['ugol_f'] = ugol_f
    shi_dli_per_plo['trub_f'] = trub_f
    shi_dli_per_plo['perimetr_f'] = perimetr_f
    shi_dli_per_plo['s_potolok_f'] = s_potolok_f
    shi_dli_per_plo['lite_f'] = lite_f
    print(shi_dli_per_plo)
    return shi_dli_per_plo

razmeri_s_d_pe_pl=poluchil_tuple_shirnu_dlinu_perim_ploshad()

def stoi_pot(razmeri_s_d_pe_pl):#, dopi ):
    numb_baget25= 0 #КРАТНЫ ПАЛКАМ 2,5М
    polotno_f=0
    total = 0
    total += razmeri_s_d_pe_pl['shirina_f']* price["brus_al"]*brus
    total += razmeri_s_d_pe_pl["ugol_f"]* price["ugol"]
    total += razmeri_s_d_pe_pl["perimetr_f"] * price["vstavka"]
    total += razmeri_s_d_pe_pl["trub_f"] * price["truba_st"]
    total += razmeri_s_d_pe_pl["lite_f"] * price["lamp"]

    if razmeri_s_d_pe_pl['shirina_f'] < 3.6:
        polotno_f= razmeri_s_d_pe_pl["s_potolok_f"] * price["polotnoMDS_320"]
        total+=polotno_f
    elif 3.6 < razmeri_s_d_pe_pl['shirina_f'] < 4.6:

        polotno_f= razmeri_s_d_pe_pl["s_potolok_f"] * price["polotnoMDS_3.6"]
        total+=polotno_f
    elif 4.6 < razmeri_s_d_pe_pl['shirina_f'] < 5.8:
        polotno_f= razmeri_s_d_pe_pl["s_potolok_f"] * price["polotnoMDS_4-5"]
        total+=polotno_f
    else:
        polotno_f = razmeri_s_d_pe_pl["s_potolok_f"] * price["polotnoMDS_4-5"]
        total += polotno_f



    # сдвинуть обсчет ниже если есть парящий потолок или \
    # теневой с вычетом длины из периметра и пересчет
    if razmeri_s_d_pe_pl["perimetr_f"]%2.5==0:
        numb_baget25= razmeri_s_d_pe_pl["perimetr_f"] * price["baget"]
        total+=numb_baget25
    elif razmeri_s_d_pe_pl["perimetr_f"]%2.5!=0:
        numb_baget25 = (razmeri_s_d_pe_pl["perimetr_f"]//2.5+1)*2.5 * price["baget"]
        total += numb_baget25


    print(
    "Полотно", polotno_f,
    "Багет" , numb_baget25,
     "Угол", razmeri_s_d_pe_pl["ugol_f"] * price["ugol"],
    "вставка", razmeri_s_d_pe_pl["perimetr_f"] * price["vstavka"],
    "трубы " , razmeri_s_d_pe_pl["trub_f"] * price["truba_st"],
        "светильники", razmeri_s_d_pe_pl["lite_f"] * price["lamp"]
    )
    print("стоимость потолка" , total , " потолка со скидкой 15% ", total*0.85, "руб.")

stoi_pot(razmeri_s_d_pe_pl)

# print(zaprose_dop_rabot)
