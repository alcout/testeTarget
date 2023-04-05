num = int(input("Digite um número: "))
fibonacci = 1
anterior = 1
penultimo = 1
IsFibonacci = False

if num == 0 or num == 1:
    IsFibonacci = True

else:
    for i in range(num):
        fibonacci = anterior + penultimo
        penultimo = anterior
        anterior = fibonacci
        if (num == fibonacci):
            IsFibonacci = True

      
if (IsFibonacci):
    print('Faz parte da sequência de Fibonacci ')
else:
    print('Não faz parte da sequência de Fibonacci ')
