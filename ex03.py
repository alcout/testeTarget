import json
from bs4 import BeautifulSoup


class dado():
    def __init__(self, dia, valor):
        self.dia = dia
        self.valor = valor


def readJson(caminho):
    arquivo = open(caminho, 'r')
    texto = arquivo.read()
    b_rows = json.loads(texto)
    dados = []

    for item in b_rows:
        dia = item['dia']
        valor = item['valor']
        d = dado(dia, valor)
        dados.append(d)

    return dados


def readXml(caminho):
    arquivo = open(caminho, 'r')
    texto = arquivo.read()
    Bs_data = BeautifulSoup(texto, "xml")
    b_rows = Bs_data.find_all('row')
    dados = []

    for item in b_rows:
        dia = item.find('dia').text
        valor = float(item.find('valor').text)
        d = dado(dia, valor)
        dados.append(d)

    return dados


def escreveDadoConsole(listaDados):
    for item in listaDados:
        print('dia:' + str(item.dia) + ' valor:' + str(item.valor))


def calculaMaiorValor(objeto):
    maior = dado(0, 0)
    for item in objeto:
        if maior.valor <= item.valor:
            maior = item
    return str(maior.valor)


def calculaMenorValor(objeto):
    menor = dado(0, 0)
    for item in objeto:
        if menor.valor >= item.valor:
            menor = item
    return str(menor.valor)


def qtdDiasUteis(objeto):
    totdias = 0
    for item in objeto:
        if item.valor > 0:
            totdias = totdias + 1
    return totdias


def mediaMensal(objeto):
    soma = 0
    for item in objeto:
        soma = soma + item.valor
    return (soma/qtdDiasUteis(objeto))


def diasSuperiorMediaMensal(objeto):
    qtdDias = 0
    mediaM = mediaMensal(objeto)
    for item in objeto:
        if item.valor > mediaM:
            qtdDias = qtdDias + 1
    return str(qtdDias)


obj01 = readJson('dados.json')
obj02 = readXml('dados.xml')


print('\n 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:')
print('\n• O menor valor de faturamento ocorrido em um dia do mês;')
print('Json ' + calculaMenorValor(obj01))
print('Xml ' + calculaMenorValor(obj02))
print('\n • O maior valor de faturamento ocorrido em um dia do mês;')
print('Json ' + calculaMaiorValor(obj01))
print('Xml ' + calculaMaiorValor(obj02))
print('\n • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.')
print('Json ' + diasSuperiorMediaMensal(obj01))
print('Xml ' + diasSuperiorMediaMensal(obj02))
