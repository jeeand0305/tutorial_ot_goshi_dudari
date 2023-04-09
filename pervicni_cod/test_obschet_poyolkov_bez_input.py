price = {"PK": 2100, "baget": 150, "polotnoMDS_320": 210,
         "polotnoMDS_4-5": 410, "NO": 500, "lamp": 350,
         "BL": 1000, "vstavka": 90, "ugol": 60, "truba_st": 350,
         "brus_al": 300
}

def decor_float_int(func):
    def wrapper(*args, **kwargs):
        # inaciliziruet function i beryt ie danie
        izm_1 = func(*args, **kwargs)
        # если число с запятой переводит с точкой
        # и присваеват тип float
        izm_1 = izm_1.replace(',', '.')
        return float(izm_1)
    return wrapper

def privet(dano):
    print("hello", dano)

def poluchil_tuple_shirnu_dlinu_perim_ploshad(list_is_telegram):
    dlina = list_is_telegram[3].replace(',', '.')
    shirina = list_is_telegram[2].replace(',', '.')
    s_potolok = list_is_telegram[4].replace(',', '.')
    ugol = list_is_telegram[5].replace(',', '.')
    trub = list_is_telegram[6].replace(',', '.')
    lite = list_is_telegram[7].replace(',', '.')

    dlina_f = float(dlina)
    shirina_f = float(shirina)
    s_potolok_f = float(s_potolok)
    ugol_f = float(ugol)
    trub_f = float(trub)
    lite_f = float(lite)
    perimetr_f=0
    shi_dli_per_plo = {}
    # if shirina > 0 and dlina > 0:
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
    elif dlina_f > 0 and s_potolok:#>0 or :
        shirina_f = s_potolok_f / dlina_f
        perimetr_f = (dlina_f+shirina_f)*2
        if dlina_f < shirina_f:
            dlina_f, shirina_f = shirina_f, dlina_f
    # elif shirina > 0 and dlina > 0 or s_potolok>0:
    elif shirina_f > 0 and dlina_f > 0 or s_potolok_f > 0:
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

# # dan=['сатин', 'ok', '2', '2', '0', '4', '2', '2', '0']
# dan2=['cfnb', 'jr', '0', '0', '13.6', '4', '1', '2', '0']
# razmeri_s_d_pe_pl=poluchil_tuple_shirnu_dlinu_perim_ploshad(dan2)
# poluchil_tuple_shirnu_dlinu_perim_ploshad(['сатин', 'ok', '2', '2', '0', '4', '2', '2', '0'])

def stoi_pot(razmeri_s_d_pe_pl):#, dopi ):
    total_dict={}
    # brus_f=brus
    brus_f=0
    numb_baget25= 0 #КРАТНЫ ПАЛКАМ 2,5М
    polotno_f=0
    total = 0
    total += razmeri_s_d_pe_pl['shirina_f']* price["brus_al"]*brus_f
    total += razmeri_s_d_pe_pl["ugol_f"]* price["ugol"]
    total += razmeri_s_d_pe_pl["perimetr_f"] * price["vstavka"]
    total += razmeri_s_d_pe_pl["trub_f"] * price["truba_st"]
    total += razmeri_s_d_pe_pl["lite_f"] * price["lamp"]
    if razmeri_s_d_pe_pl['shirina_f'] < 3.6:
        polotno_f= razmeri_s_d_pe_pl["s_potolok_f"] * price["polotnoMDS_320"]
        total+=polotno_f
    elif razmeri_s_d_pe_pl['shirina_f'] > 3.6:
        polotno_f= razmeri_s_d_pe_pl["s_potolok_f"] * price["polotnoMDS_4-5"]
        total+=polotno_f

    # сдвинуть обсчет ниже если есть парящий потолок или \
    # теневой с вычетом длины из периметра и пересчет
    if razmeri_s_d_pe_pl["perimetr_f"]%2.5==0:
        numb_baget25= razmeri_s_d_pe_pl["perimetr_f"] * price["baget"]
        total+=numb_baget25
    elif razmeri_s_d_pe_pl["perimetr_f"]%2.5!=0:
        numb_baget25 = (razmeri_s_d_pe_pl["perimetr_f"]//2.5+1)*2.5 * price["baget"]
        total += numb_baget25
    total_dict[1]=total
    total_dict[2] = total*0.85

    print(
    "Полотно", polotno_f,
    "Багет" , numb_baget25,
     "Угол", razmeri_s_d_pe_pl["ugol_f"] * price["ugol"],
    "вставка", razmeri_s_d_pe_pl["perimetr_f"] * price["vstavka"],
    "трубы " , razmeri_s_d_pe_pl["trub_f"] * price["truba_st"],
        "светильники", razmeri_s_d_pe_pl["lite_f"] * price["lamp"]
    )
    print("стоимость потолка" , total , " потолка со скидкой 15% ", total*0.85, "руб.")
    return total_dict

# stoi_pot(razmeri_s_d_pe_pl)

# print(zaprose_dop_rabot)
