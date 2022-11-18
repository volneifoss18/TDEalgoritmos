listaNomes = []
quantidadeNomes = int(input("Digite a quantidade de nomes a cadastrar: "))
count = 0

while count < quantidadeNomes:
    
    listaNomes.append(input("Digite o nome: "))
    count += 1

for i in listaNomes:
    print(i)