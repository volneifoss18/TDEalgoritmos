listaNumeros = []

for i in range(8):
    listaNumeros.append(int(input("Digite um numero: ")))

soma = 0    
for i in listaNumeros:
    if i > 30:
        soma += i

print(soma)