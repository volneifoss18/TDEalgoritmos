listaCompras = []

continuar = True
while continuar == True:
    print("\nEscolha a opção: ")
    opcao = int(input("[0] para sair \n[1] para adicionar produto \n[2] para remover produto \nDigite o numero desejado: "))
    
    match opcao:
        case 0 :
            continuar = False
        case 1 : 
            listaCompras.append(input("Digite o produto a cadastrar: "))
        case 2 : 
            listaCompras.remove(input("Digite o produto a ser removido: "))
        case _ : 
            print("Digite uma opção valida")
            
for i in listaCompras:
    print(f'\nproduto : {i}')