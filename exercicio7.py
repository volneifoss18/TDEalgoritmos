listaNumeros = []
numerosPares = []
numerosImpares = []

for i in range(10):
    listaNumeros.append(int(input("Digite um número: ")))

for i in listaNumeros:
    if i % 2 == 0:
        numerosPares.append(i)
    elif i % 2 != 0:
        numerosImpares.append(i)
        
for i in numerosPares:
    print(f'numero par : ${i}')

for i in numerosImpares:
    print(f'numero impar : ${i}')
