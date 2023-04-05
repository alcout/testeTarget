SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
Outros = 19849.53
total = SP + RJ + MG + ES + Outros


def calculaPercentual(valorEstado):
    return f'{(valorEstado/total * 100):.2f}%'


print('O percentual de SP foi: ' + calculaPercentual(SP))
print('O percentual de RJ foi: ' + calculaPercentual(RJ))
print('O percentual de MG foi: ' + calculaPercentual(MG))
print('O percentual de ES foi: ' + calculaPercentual(ES))
print('O percentual de Outros foi: ' + calculaPercentual(Outros))
