import json

ar=[]

with open("cenz.txt", 'r', encoding="cp1251") as r:
    for i in r:
        n = i.lower().split('\n')[0]
        if n != '':
            ar.append(n)

with open("cenz.json", "w", encoding='utf-8') as e:
    json.dump(ar,e)
