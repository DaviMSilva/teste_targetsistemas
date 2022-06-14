import json
def representacao(arq):
    with open(arq, encoding='utf-8') as dadosJson:
        dados = json.load(dadosJson)

    total = 0
    for i in dados:
        total += i['faturamento']
    print("Faturamento total = ", total)
    print("porcentagens....")
    for i in dados:
        porc = i['faturamento']/total *100

        print(i['estado'] , "representa: ", round(porc,2) ,"%")

representacao('q4.json')