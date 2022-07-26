



import json
class faturadiario():
    def menorFaturamento(dadoJson):
        json_dado = open(dadoJson,encoding='utf-8' )
        
        dados = json.load(json_dado)

        menorFaturamento = -1
        for i in dados:
            if menorFaturamento == -1:
                menorFaturamento = i['valor']

            if i['valor'] < menorFaturamento and i['valor'] != 0:
                menorFaturamento = i['valor']
        
        print(menorFaturamento)

    def maiorFaturamento(dadoJson):
        json_dado = open(dadoJson,encoding='utf-8' )
        
        dados = json.load(json_dado)

        maiorFaturamento = 0
        for i in dados:

            if i['valor'] > maiorFaturamento:
                maiorFaturamento = i['valor']
        
        print(maiorFaturamento)

    def mediaFaturamento(dadoJson):
        json_dado = open(dadoJson,encoding='utf-8' )
        
        dados = json.load(json_dado)

        somaTotal = 0
        diasTotal = 0
        for i in dados:
            if i['valor'] != 0:
                somaTotal += i['valor']
                diasTotal+=1
        
        media = somaTotal/diasTotal
        return media
    
    def diasSuperiorMedia(media, dadoJson):
        json_dado = open(dadoJson,encoding='utf-8' )
        
        dados = json.load(json_dado)

        
        diasSuperior = 0
        for i in dados:
            if i['valor'] > media:
                
                diasSuperior+=1
        
        
        print(diasSuperior)

arq = 'dados.json'
print('maior valor :' )
faturadiario.maiorFaturamento(arq)

print('menor valor diferente de zero')
faturadiario.menorFaturamento(arq)

media = faturadiario.mediaFaturamento(arq)
print('Media: ', media)

print('dias Superiores a media: ')
faturadiario.diasSuperiorMedia(media, arq)