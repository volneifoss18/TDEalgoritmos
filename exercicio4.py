listaNumeros = []

count = 0
while count < 5:
    listaNumeros.append(int(input("digite um numero")))
    count += 1

total = 0
for i in listaNumeros:
    total += i
    
print(total)