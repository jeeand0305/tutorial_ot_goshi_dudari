

price={"PK":2100, "baget":150, "polotnoMDS_320":210, "NO":500, \
       "lamp":350, "BL":1000 }


print("Краткие обозночение элементов потолка")
print("при выборе доп элементов потолка нужно вписать ")
print("краткое нименование слитно с количеством ")
print("использовать только латинские заглавные буквы")
print("ПРИМЕР", "PK2, NO5")

# print( PK )


shirina = int(input("Введи ширину комноты если нет пиши 0 : "))
dlina = int(input("Введи длину комноты если нет пиши 0: "))
s_potolok = int(input("Введи площадь комноты если нет пиши 0:"))
zaprose_dop_rabot=input("Дополнительные количество работ :")

print(zaprose_dop_rabot)

def poluchil_tuple_shirnu_dlinu_perim_ploshad():
    dlina_f = dlina
    shirina_f = shirina
    s_potolok_f = s_potolok
    shi_dli_per_plo = {}
    if shirina > 0 and dlina > 0:
        s_potolok_f = dlina_f*shirina_f
        perimetr_f = (dlina_f+shirina_f)*2
        # замена ширины и длины между собой
        if dlina_f <= shirina_f:
            dlina_f, shirina_f = shirina_f, dlina_f
    elif shirina > 0 and s_potolok:#>0 or dlina > 0:
        dlina_f = s_potolok_f / shirina_f
        perimetr_f = (dlina_f+shirina_f)*2
        if dlina_f < shirina_f:
            dlina_f, shirina_f = shirina_f, dlina_f
    elif dlina_f > 0 and s_potolok:#>0 or :
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
    shi_dli_per_plo['perimetr_f'] = perimetr_f
    shi_dli_per_plo['s_potolok_f'] = s_potolok_f
    print(shi_dli_per_plo)
    return shi_dli_per_plo

razmeri_s_d_pe_pl=poluchil_tuple_shirnu_dlinu_perim_ploshad()

def stoi_pot(razmeri_s_d_pe_pl):#, dopi ):
    numb_baget25= 0 #КРАТНЫ ПАЛКАМ 2,5М
    total = 0
    total += razmeri_s_d_pe_pl["s_potolok_f"] * price["polotnoMDS_320"]
    numb_baget25 = razmeri_s_d_pe_pl["perimetr_f"]//2.5



    # сдвинуть обсчет ниже если есть парящий потолок или \
    # теневой с вычетом длины из периметра и пересчет
    if numb_baget25 == razmeri_s_d_pe_pl["perimetr_f"]/2.5:
        numb_baget25 = perimetr_f * price["baget"]
    elif numb_baget25 != razmeri_s_d_pe_pl["perimetr_f"]/2.5:

        numb_baget25= ((numb_baget25+1)*2.5) * price["baget"]
    print("Стоимость багета", numb_baget25)
    total+= numb_baget25
    print("стоимость потолка", total, "руб.")

stoi_pot(razmeri_s_d_pe_pl)

print(zaprose_dop_rabot)

