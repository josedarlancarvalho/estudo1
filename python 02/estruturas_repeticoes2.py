#WHILE

opcao = -1

while opcao != 0:
    opcao = int(input("escolha uma opcao 1- extrato /n 2- saldo / 0- sair"))

    if opcao == 1:
        print("extrato")
    elif opcao ==2:
        print ("saldo")

#o while é tipo um if, porem, o if so faz uma vez, ja o while pode repetir infinitamente.


#break. ele para quando algo acontece, ou seja, eu digo onde eu quero que o programa pare de rodar

while True:
    opcao = int(input("digite um numero: "))
    if opcao == 5:
        break

    print(opcao)


for opcao in range (199):
    if opcao == 10:
        break

    print(opcao)

#continue, é um negocio diferente do break, ele faz continuar o codigo porem, pulando algo.


for opcao in range (199):
    if opcao == 10:
        continue

    print(opcao)
#aqui ele vai pular o 10. vai exibir todos os numeros de 0 a 198, menos o 10.
#ele server bem para achar numero impar ou pa numa sequencia.


for opcao in range (199):
    if opcao % 2 == 0:
        break

    print(opcao)

#aqui ele vai exibir os numeros pares, % é o resto da divisao, ou seja, ele dividiu por 2 e se o resto por 0 ele é par e continuou o codigo