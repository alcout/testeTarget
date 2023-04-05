palavra = input("Digite uma palavra: ")
index = len(palavra) - 1
invertido = ''

for letra in palavra:
    invertido = invertido + (palavra[index])
    index = index - 1
print(invertido)