listaNumeros = []

count = 0
while count < 6:
    listaNumeros.append(int(input("digite um numero")))
    listaNumeros.sort(reverse=True)
    count += 1

for i in listaNumeros:
    print(i -1)    
    
print(listaNumeros)
