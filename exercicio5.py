listaNumeros = []
for i in range(10):
    listaNumero = int(input("Digite um numero"))
    listaNumeros.append(listaNumero)
    if listaNumero == 99:
        break
    
soma = sum (listaNumeros)
tamanho = len(listaNumeros)
media = soma / 2
print(soma)
print(tamanho)
print(media)

